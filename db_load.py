import gzip
import time
from math import ceil

import pandas as pd
import sqlalchemy.types as SQLAT
import yaml
from sqlalchemy import text

import mydbconnection as mdbcon


def convert_dtype(types: dict) -> dict:

    conv = {
        'VARCHAR':  SQLAT.VARCHAR,
        'SMALLINT': SQLAT.SMALLINT,
        'BOOLEAN':  SQLAT.BOOLEAN,
        'INTEGER':  SQLAT.INTEGER,
        'FLOAT':    SQLAT.FLOAT
    }

    return {k: conv[v]() if len(v.split()) == 1 else conv[v.split()[0]](int(v.split(maxsplit=1)[1])) for k, v in types.items()}


##### Chargement des configs
config = yaml.safe_load(open("config_db_load.yaml", 'r'))

param = config['param']

##### Params
ch_size = param['chunksize']
doss = param['folder']

section = param['config_file_section']

##### Connexion bdd
print(f"\nConnexion à '{section}'...")
conn = mdbcon.create_db(param['connection_config_file'], section)

if conn == None:
    quit()

print('Connexion établie !', end='\n\n')

##### Boucle création des tables
table_names = list(config['files'].keys())
global_time = time.time()

n_file = 0
for tn in table_names:

    n_file += 1
    file_time = time.time()

    current_file = config['files'][tn]
    path = f"{doss}/{current_file['name_file']}"

    print(f"{n_file:2}/{len(table_names)} - {tn} - get nb_lines : ", end='')
    nb_lines = sum(1 for _ in gzip.open(path)) - 1
    print(f"{nb_lines:,}")

    nb_chunks = ceil(nb_lines / ch_size)

    column_types = convert_dtype(current_file['column_types'])

    with pd.read_csv(path, sep='\t', na_values=current_file['na_values'], quoting=3, low_memory=False, chunksize=ch_size) as chunk_it:

        if_ex = 'replace'

        n = 0
        for df in chunk_it:

            lines_time = time.time()

            if 'explode_on' in current_file:

                explode_on = current_file['explode_on']

                new_name = explode_on if 'explode_new_name' not in current_file else current_file['explode_new_name']

                df[new_name] = df[explode_on].apply(lambda x: str(x).split(','))

                df = df.explode(new_name).dropna()

            df = df[list(column_types.keys())]

            df.to_sql(tn, conn, dtype = column_types, if_exists=if_ex, index=False)

            if_ex = 'append'
            n += 1
            d = time.time() - lines_time
            d = f"{int(d)} s" if d < 60 else f"{d/60:.1f} m"
            print(f" - {n_file:2}/{len(table_names)} - {tn} : {n:5,} / {nb_chunks:,}  -  {n/nb_chunks:8.3%}  -  {d}")

    conn.execute(text(f"ALTER TABLE {tn} ADD PRIMARY KEY ({','.join(current_file['primary_keys'])});"))

    if 'foreign_keys' in current_file:
        for frkey in current_file['foreign_keys']:
            conn.execute(text(f"ALTER TABLE {tn} ADD FOREIGN KEY ({frkey}) REFERENCES {current_file['foreign_keys'][frkey]}"))

    d = time.time() - file_time
    m = int(d/60)
    s = int(d%60)

    print(f" ----- {m:3} m {s:02}", end='\n\n')

# Commit pour être sûr
conn.commit()

# Calcul du temps mis
d = time.time() - global_time
h = f"{int(d/3600):3} h"
d %= 3600
m = f"{int(d/60):02} m"
s = f"{int(d%60):02}"

print("Temps total :", h, m, s)

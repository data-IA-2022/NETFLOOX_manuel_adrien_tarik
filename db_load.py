import mydbconnection as mdbcon
from sqlalchemy import text
import sqlalchemy.types as SQLAT
import pandas as pd
import time
import datetime
import numpy as np
import gzip
from math import ceil

# Connect to the database using an SSH tunnel
section = 'mysql_azure_netfloox'
print(f"\nConnexion à {section}...", end='')
conn = mdbcon.connect_to_db('config.yaml', section)
print('ok', end='\n\n')

# # Connect to the database directly
# conn = mdbcon.connect_to_db('config.ini', 'mydb', ssh=False)

dtype= {
    'nconst':               SQLAT.VARCHAR(10),
    'tconst':               SQLAT.VARCHAR(10),
    'ordering':             SQLAT.SMALLINT(),  # title.akas title.principals

    ### name.basics
    'primaryName':          SQLAT.VARCHAR(300),
    'birthYear':            SQLAT.SMALLINT(),
    'deathYear':            SQLAT.SMALLINT(),
    'primaryProfession':    SQLAT.VARCHAR(300),

    ### title.akas
    'titleId':              SQLAT.VARCHAR(10),
    'title':                SQLAT.VARCHAR(1000),
    'region':               SQLAT.VARCHAR(5),
    'language':             SQLAT.VARCHAR(5),
    'types':                SQLAT.VARCHAR(40),
    'attributes':           SQLAT.VARCHAR(255),
    'isOriginalTitle':      SQLAT.BOOLEAN(),

    ### title.basics
    'titleType':            SQLAT.VARCHAR(15),
    'primaryTitle':         SQLAT.VARCHAR(500),
    'originalTitle':        SQLAT.VARCHAR(500),
    'isAdult':              SQLAT.BOOLEAN(),
    'startYear':            SQLAT.SMALLINT(),
    'endYear':              SQLAT.SMALLINT(),
    'runtimeMinutes':       SQLAT.INTEGER(),
    'genres':               SQLAT.VARCHAR(100),

    ### title.crew SPECIAL

    ### title.episode
    'parentTconst':         SQLAT.VARCHAR(10),
    'seasonNumber':         SQLAT.SMALLINT(),
    'episodeNumber':        SQLAT.SMALLINT(),

    ### title.principals
    'category':             SQLAT.VARCHAR(20),
    'job':                  SQLAT.VARCHAR(300),
    'characters':           SQLAT.VARCHAR(1400),

    ### title.ratings
    'averageRating':        SQLAT.FLOAT(),
    'numVotes':             SQLAT.INTEGER()
}

doss = "data"
file_names = ("name.basics.tsv.gz", "title.akas.tsv.gz", "title.basics.tsv.gz", "title.crew.tsv.gz", "title.episode.tsv.gz", "title.principals.tsv.gz", "title.ratings.tsv.gz")
ch_size = 1000000

start_time_global = time.time()

n_file = 0
for fn in file_names:

    n_file += 1
    file_time = time.time()
    path = f"{doss}/{fn}"
    fns = fn.removesuffix('.tsv.gz').replace('.', '_')

    print(f"{n_file:2}/{len(file_names)} - {fns} - get nb_lines : ", end='')
    nb_lines = sum(1 for _ in gzip.open(path)) - 1
    print(nb_lines)

    nb_chunks = ceil(nb_lines / ch_size)

    with pd.read_csv(path, sep='\t', na_values=('\\N', 'N'), quoting=3, low_memory=False, chunksize=ch_size) as chunk_it:

        if_ex = 'replace'

        n = 0
        for df in chunk_it:

            if fns == "title_crew":

                df_dir = df.assign(nconst = df['directors'].str.split(','))[['nconst', 'tconst']].explode('nconst').dropna()
                df_wri = df.assign(nconst = df['writers'].str.split(','))[['nconst', 'tconst']].explode('nconst').dropna()

                df_dir.to_sql(fns + "_directors", conn, dtype = dtype, if_exists=if_ex, index=False)
                df_wri.to_sql(fns + "_writers", conn, dtype = dtype, if_exists=if_ex, index=False)

            if fns == "name_basics":

                df_knf = df.assign(tconst = df['knownForTitles'].str.split(','))[['nconst', 'tconst']].explode('tconst').dropna()

                df.drop(columns='knownForTitles').to_sql(fns, conn, dtype = dtype, if_exists=if_ex, index=False)
                df_knf.to_sql(fns + "_knowForTitles", conn, dtype=dtype, if_exists=if_ex, index=False)

            else:

                df.to_sql(fns, conn, dtype = dtype, if_exists=if_ex, index=False)

            if_ex = 'append'

            n += 1
            print(f" - {n_file:2}/{len(file_names)} - {fns} : {n:5,} / {nb_chunks:,}  -  {n/nb_chunks:7.4%}")

    d = time.time() - file_time
    m = int(d/60)
    s = int(d%60)

    print(f" ----- {m:3} m {s:02}", end='\n\n')

d = time.time() - start_time_global
h = int(d/3600)
d %= 3600
m = int(d/60)
s = int(d%60)

print(f"finif - {h:3} h {m:02} m {s:02}")

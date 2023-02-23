import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import RobustScaler, MinMaxScaler
from sqlalchemy import text

import db_connection as db_con
from os.path import exists, join, dirname, basename
import pickle
from math import ceil
import time


def calc_time(start_time):

    d = time.time() - start_time
    h = int(d / 3600)
    h = f"{h} h " if d > 3600 else ''
    m = int(d % 3600 / 60)
    m = f"{m} m " if d > 60 else ''
    s = int(d % 3600 % 60)
    s = f"{s} s"
    return h + m + s


def dl_data_from_db(list_columns, table, where, verbose):

    sql = text(f"SELECT {', '.join(list_columns)} FROM {table} {where}")

    path_config = join(dirname(__file__), 'config.yaml')
    conn = db_con.connect_to_db(path_config, "mysql_azure_netfloox")

    if verbose: print("-> requête sql... ", end='')

    nombre_lines = conn.execute(text(f"SELECT COUNT(*) FROM {table} {where}")).scalar()

    if verbose:
        print(f"{nombre_lines:,} lignes", end='\n\n')
        start_time = time.time()

    dfs = []
    chunksize = 1_000_000
    n_chunks = ceil(nombre_lines/chunksize)

    n = 0
    for chunk in pd.read_sql(sql, conn, chunksize=chunksize):

        n += 1
        dfs.append(chunk)

        if verbose: print(f"{n:3} / {n_chunks} - {n/n_chunks:8.3%}")

    conn.close()
    
    if verbose:
        print('\n', calc_time(start_time))

        print("\nConcaténation... ", end='')
        start_time = time.time()

    df = pd.concat(dfs)

    if verbose: print('ok\n', calc_time(start_time), end='\n\n')

    return df


def get_data(path_file, verbose = False):

    if verbose:
        print(f"\nRécupération de {basename(path_file)}")
        global_time = time.time()

    if not exists(path_file):

        if verbose: print(f"\n{basename(path_file)} n'existe pas\n\nRécupération depuis la base de données")

        list_columns = ['tconst', 'originalTitle', 'runtimeMinutes', 'isAdult', 'startYear', 'genres', 'averageRating', 'numVotes', 'nconst_staf', 'category']
        table = 'table_films_2'
        where = ""

        df = dl_data_from_db(list_columns, table, where, verbose)

        if verbose:
            print("Pivot... ", end='')
            start_time = time.time()

        df = pd.pivot_table(df, index=list_columns[:-2], values='nconst_staf', columns='category', aggfunc=lambda x: ','.join(x.unique())).reset_index()

        if verbose: print('ok\n', calc_time(start_time), end='\n\n')

        for c in df.select_dtypes(include='object').columns:

            df[c] = df[c].fillna('')

        for c in df.select_dtypes(exclude='object').columns:

            df[c] = df[c].fillna(0)

        df_noms = df[['tconst', 'originalTitle']]

        df.drop(columns='tconst', inplace=True)

        columns_CountV = df.select_dtypes(include='object')

        columns_pass   = ['isAdult', 'averageRating']
        columns_MinMax = ['startYear']
        columns_Robust = ['runtimeMinutes', 'numVotes']

        transformers = [
            ('col_runtime', RobustScaler(), columns_Robust),
            ('col_pass', 'passthrough', columns_pass),
            ('col_year', MinMaxScaler(), columns_MinMax),
        ] + [('col_' + cc, CountVectorizer(), cc) for cc in columns_CountV]

        preparation = ColumnTransformer(transformers)

        if verbose:
            print("Preparation des données... ", end='')
            start_time = time.time()

        df_prep = preparation.fit_transform(df)

        if verbose: print('ok\n', calc_time(start_time), end='\n\n')

        pickle.dump((df_noms, df_prep), open(path_file, 'wb'))

    else:

        df_noms, df_prep = pickle.load(open(path_file, 'rb'))

    if verbose: print('Création / Récupération des datas : ', calc_time(global_time), end='\n\n')
    return df_noms, df_prep


def get_index(value, array):

    return array[array == value].index[0]


def get_best(list_, num):

    if len(list_) <= num:

        return sorted(list_, key=lambda x:x[1], reverse=True)

    mid = len(list_)//2
    list_ = get_best(list_[:mid], num) + get_best(list_[mid:], num)

    return sorted(list_, key=lambda x:x[1], reverse=True)[:num]


class Model_reco:


    def __init__(
        self,
        path_file = join(dirname(dirname(__file__)), 'data', 'data_recommandation.data'),
        verbose   = False
    ):

        self.path_file = path_file
        self.verbose   = verbose

        self.noms_films, self.data_prep = get_data(path_file, verbose)


    def get_reco(self, value, best_of : int, by = 'originalTitle'):

        try:
            index_y = get_index(value, self.noms_films[by])
        except IndexError:
            print(f"Le film '{value}' n'existe pas dans la collone {by}.")
            return pd.DataFrame(columns=['score', 'tconst', 'originalTitle'])

        if self.verbose:
            print("Calcul des similaritées... ", end='')
            start_time = time.time()

        list_sim = cosine_similarity(self.data_prep, Y=self.data_prep[index_y])

        if self.verbose:
            print('ok\n', calc_time(start_time), end='\n\n')

            print("Trie... ", end='')
            start_time = time.time()

        list_sim = get_best(list(enumerate(list_sim)), best_of)

        if self.verbose:
            print('ok\n', calc_time(start_time), end='\n\n')

        df = pd.DataFrame()

        list_index, list_score = zip(*list_sim)

        df['score']         = [s.item(0) for s in list_score]
        df['tconst']        = [self.noms_films['tconst'][id] for id in list_index]
        df['originalTitle'] = [self.noms_films['originalTitle'][id] for id in list_index]

        return df


def main():

    model = Model_reco(verbose=True)

    df = model.get_reco('Star Wars: The Clone Wars', 11)

    print(df)


if __name__ == '__main__':
    main()
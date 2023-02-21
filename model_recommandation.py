import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sqlalchemy import text

import db_connection as db_con
from os.path import exists
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


path_df = "data/table_films_2.df"

list_columns = ['tconst', 'titleType', 'originalTitle', 'runtimeMinutes', 'isAdult', 'startYear', 'genres', 'nconst_director', 'nconst_writer', 'averageRating', 'numVotes', 'nconst_staf', 'category', 'characters']
table = 'table_films_2'

where = "WHERE category NOT IN ('director', 'writer')"

sql = text(f"SELECT {', '.join(list_columns)} FROM {table} {where}")

print(f"load {path_df}")
start_time = time.time()

if not exists(path_df):

    print(f"{path_df} n'existe pas\n-> création... ", end='')
    conn = db_con.connect_to_db('config.yaml', 'mysql_azure_netfloox')

    nombre_lines = conn.execute(text(f"SELECT COUNT(*) FROM {table} {where}")).scalar()
    print(f"{nombre_lines:,} lignes", end='\n\n')

    dfs = []
    chunksize = 1_000_000
    n_chunks = ceil(nombre_lines/chunksize)

    n = 0
    for chunk in pd.read_sql(sql, conn, chunksize=chunksize):

        chunk_time = time.time()
        n += 1
        dfs.append(chunk)

        print(f"{n:3} / {n_chunks} - {n/n_chunks:8.3%} - {calc_time(chunk_time)}")

    print("\nConcaténation...", end='')
    df = pd.concat(dfs)
    print('ok', end='\n\n')

    pickle.dump(df, open(path_df, 'wb'))

else:

    df = pickle.load(open(path_df, 'rb'))

print('-----', calc_time(start_time), end='\n\n')

df_piv = pd.pivot_table(df, index=['tconst'], values='nconst_staf',columns= 'category', aggfunc=','.join)

print(df.columns)
print(df_piv.columns)

quit()

#Ajout du ratting et numVote
recommendation = df_recommendation.drop(columns = ['originalTitle'])
recommendation['reco_vector'] = recommendation.iloc[:, 1:].apply(' '.join, axis=1)

#on ajoute le nom du film
recommendation = recommendation.join(df_recommendation['originalTitle'])
recommendation = recommendation[['tconst', 'reco_vector', 'originalTitle']]

df.drop(columns=['tconst', 'originalTitle'])

#fonction qui retrouve le titre du film en fonction de l'index
find_title_from_index = lambda index: recommendation[recommendation.index == index]["originalTitle"].values[0]

#fonction qui retrouve l'index du film en fonction du titre
find_index_from_title = lambda title: recommendation[recommendation.originalTitle == title].index.values[0]

movie = "Star Wars: Episode I - The Phantom Menace"
movie_index = find_index_from_title(movie)

# Déclaration de la méthode de vectorisation et application
cv = CountVectorizer()
count_matrix = cv.fit_transform(recommendation['reco_vector'])

count_matrix[movie_index]

# Calcul des similarités uniquement pour le film en question pour limiter la taille de la matrice
cosine_sim = cosine_similarity(count_matrix, Y= count_matrix[movie_index])

sorted_similar_movies = sorted(list(enumerate(cosine_sim)), key=lambda x:x[1], reverse=True)[1:6]

for id_film, score in sorted_similar_movies:
    print(score, find_title_from_index(id_film))

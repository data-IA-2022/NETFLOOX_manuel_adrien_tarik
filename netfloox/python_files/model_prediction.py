import pandas as pd
import time
from os.path import exists
from .utils import calc_time, relative_path
from sqlalchemy import text
import pickle
import python_files.db_connection as db_con

from sklearn.preprocessing import LabelEncoder, OneHotEncoder, RobustScaler
from sklearn.impute import KNNImputer, SimpleImputer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn import set_config
from sklearn.ensemble import RandomForestRegressor, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import confusion_matrix, accuracy_score, ConfusionMatrixDisplay, f1_score, fbeta_score, r2_score


def create_df_for_dataset(path):

    #connection à la base
    try: 
        conn = db_con.connect_to_db(relative_path('python_files', 'config.yaml'), "mysql_azure_netfloox")
    except ValueError:
        print("Could not connect to database.")
        quit()

    # création des dfs
    # SQL query pour récupérer les donnéés qui vont bien et les mettres dans nos df 
    query = text("""
        SELECT tconst, originalTitle, category, primaryName, runtimeMinutes, isAdult, startYear, genres, averageRating
        FROM netfloox_db.table_films_2
        WHERE category IN ('actor','actress','director','composer');
    """)
    # column names
    df = pd.read_sql_query(query, conn)
    print(df.head(3))
    # pivot table pour tout rapporter à la maille film selection des colonnes nécéssaires
    df_subset_for_pivot = df[["tconst","primaryName","category"]]#.query('category in ("actor","actress","director","composer")')

    #le pivot
    principals = pd.pivot_table(df_subset_for_pivot, index=['tconst'], values='primaryName',columns= 'category',
                        aggfunc=lambda x: ','.join(x), fill_value='')
    #le reste des colonnes 
    df_not_pivot = df[["tconst", "originalTitle",	"averageRating", "runtimeMinutes",	"isAdult", "startYear",	"genres",]].groupby(df['tconst']).aggregate('first')

    #Join des tables sur le tconst
    df_not_pivot = df[["tconst", "originalTitle",	"averageRating", "runtimeMinutes",	"isAdult", "startYear",	"genres",]].groupby(df['tconst']).aggregate('first')
    df_prediction = pd.merge(df_not_pivot, principals, how='inner', left_on = df_not_pivot['tconst'], right_on = principals.index)
    df_prediction.drop('key_0', inplace=True, axis=1)
    #suppression des na
    df_prediction.dropna(inplace=True)

    #drop de tconst pour le dataset
    df_prediction.drop(columns=['tconst'],inplace=True)

    # Save the Dataset prédiction in a serialized format
    df_prediction.to_pickle(path)

    return df_prediction


def get_dataset():

    path = relative_path('data', 'dataset_prediction.pickle')

    if not exists(path):
        dataset = create_df_for_dataset(path)
    else:
        dataset =  pickle.load(open(path, 'rb'))

    return dataset


def get_features_target(dataset):

    y = dataset['averageRating']
    X = dataset.drop(columns=['averageRating'])

    return X, y


def get_pipeline_preparation(X):

    #Sélections des variables catégorielles et numériques
    column_cat = X.select_dtypes(include=['object']).columns
    column_num = X.select_dtypes(exclude=['object']).columns

    #Transformation des données cat et num
    #Pas d'imputation içi remplacer les éléments manquants par des acteurs non présents dans les films non renseignés n'a aucun intérêt.
    transfo_cat = Pipeline(steps=[
        ('bow', CountVectorizer())
        #('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output = False))
    ])

    # Je choisi içi un robustScaler a cause de la colonne runtimeMinutes qui dispose d'outliers 1min à des milliers de min
    transfo_num = Pipeline(steps=[
        ('imputation', KNNImputer(n_neighbors=3, weights="uniform")),
        ('scaling', RobustScaler())
    ])

    transformers = [('data_num', transfo_num , column_num)] + [('data_' + cc, transfo_cat, cc) for cc in column_cat]

    #Transformation des features
    preparation = ColumnTransformer(
        transformers=transformers
    )
    print("fin de l'étape de préparation")

    return preparation


def get_pipeline_model(prepa, model):

    pipeline = Pipeline([('preparation', prepa),
        #('pca',PCA()),
        ('model',model)]
    )

    return pipeline


def grid_search(pipeline, X, y):

    param_grid = [
        {
            'model': [RandomForestRegressor()],
            'model__n_estimators': range(100, 701, 50),
            'model__max_depth': range(3, 15),
            'pca__n_components': range(10, 51, 10),
        }#,
        # {
        #     'model': [KNeighborsRegressor()],
        #     'model__n_neighbors': [3, 5, 7],
        #     'model__weights': ['uniform', 'distance'],
        #     'pca__n_components': [10, 20, 30],
        # }
    ]

    grid_search = GridSearchCV(pipeline, param_grid, cv=5, verbose= 3)
    grid_search.fit(X, y)

    return grid_search


def main():

    start_time = time.time()

    dataset = get_dataset()
    print(dataset.columns)
    print(dataset.shape)
    print(dataset.isna().sum())
    print(dataset.head(3))

    X, y = get_features_target(dataset)

    prepa = get_pipeline_preparation(X)
    model = RandomForestRegressor()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

    #pipe_model = get_pipeline_model(prepa, model)
    #pipe_model.fit(X_train, y_train)

    pipe_model = get_pipeline_model(prepa, model)
    print(pipe_model)
    gridS = grid_search(pipe_model, X, y)
    print(gridS.best_params_, gridS.best_estimator_)

    path = relative_path('modeles', 'gridS.model')
    pickle.dump(gridS, open(path, 'wb'))

    y_pred = gridS.predict(X_test)
    score = r2_score(y_test, y_pred)
    print("Performance du modèle RandomForestRegressor - Accuracy score :", round(score, 5))

    print("Temps total :", calc_time(start_time))


if __name__ == '__main__':
    main()

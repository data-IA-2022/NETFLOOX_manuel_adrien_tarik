import pandas as pd
from sqlalchemy import create_engine

# Créer une connexion SQLAlchemy
engine = create_engine('mysql+pymysql://root:greta2023@greta-p2-g3.westeurope.cloudapp.azure.com/netfloox_db')

datasets = {'tables' : {'films' : pd.read_pickle('./projet_netfloox/dataset_prédiction.pickle')},
            'analyses': {'notes' : pd.read_sql_table('table_distrib_notes', engine),
                         'types' : pd.read_sql_table('table_distrib_types', engine),
                         'decenie_votes_rating' : pd.read_sql_table('table_decenie_votes_rating', engine),
                         'prop_notes_null' : pd.read_sql_table('table_prop_notes_null', engine),
                         'region_diffusion_films' : pd.read_sql_table('table_region_len2_diffusion_films', engine),
                         'classement_regions_production_films' : pd.read_sql_table('vue_classement_regions_production_films', engine),
                         'region_len2_stats_films' : pd.read_sql_table('table_region_len2_stats_films', engine),
                         'region_stats_films' : pd.read_sql_table('table_region_stats_films', engine)}}

engine.dispose()

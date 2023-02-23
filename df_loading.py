import pandas as pd
from db_connection import connect_to_db
import yaml

# Créer une connexion SQLAlchemy
config = yaml.safe_load(open("..\\config_db_load.yaml", 'r'))
engine = connect_to_db(config['param']['connection_config_file'], 'mysql_azure_netfloox_Ex')

datasets = {'tables' : {'films' : pd.read_pickle('./projet_netfloox/dataset_prédiction.pickle')},
            'analyses': {'notes' : pd.read_sql_table('table_distrib_notes', engine),
                         'types' : pd.read_sql_table('table_distrib_types', engine),
                         'films_votes_rating_annee' : pd.read_sql_table('table_list_films_ex', engine),
                         'decenie_votes_rating' : pd.read_sql_table('table_decenie_votes_rating', engine),
                         'prop_notes_null' : pd.read_sql_table('table_prop_notes_null', engine),
                         'region_diffusion_films' : pd.read_sql_table('table_region_len2_diffusion_films', engine),
                         'classement_regions_production_films' : pd.read_sql_table('vue_classement_regions_production_films', engine),
                         'region_len2_stats_films' : pd.read_sql_table('table_region_len2_stats_films', engine),
                         'region_stats_films' : pd.read_sql_table('table_region_stats_films', engine)}}
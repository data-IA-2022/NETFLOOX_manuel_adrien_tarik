import pandas as pd
from .db_connection import connect_to_db
import yaml
import os

doss_python_files = os.path.dirname(__file__)
path_config = os.path.join(doss_python_files, 'config.yaml')
path_dataset = os.path.join(os.path.dirname(doss_python_files), 'data', 'dataset_prédiction.pickle')

conn = connect_to_db(path_config, 'mysql_azure_netfloox')

datasets = {'tables' : {'films' : pd.read_pickle(path_dataset)},
            'analyses': {'notes' : pd.read_sql_table('table_distrib_notes', conn),
                         'types' : pd.read_sql_table('table_distrib_types', conn),
                         'films_votes_rating_annee' : pd.read_sql_table('table_list_films_ex', conn),
                         'decenie_votes_rating' : pd.read_sql_table('table_decenie_votes_rating', conn),
                         'prop_notes_null' : pd.read_sql_table('table_prop_notes_null', conn),
                         'region_diffusion_films' : pd.read_sql_table('table_region_len2_diffusion_films', conn),
                         'classement_regions_production_films' : pd.read_sql_table('vue_classement_regions_production_films', conn),
                         'region_len2_stats_films' : pd.read_sql_table('table_region_len2_stats_films', conn),
                         'region_stats_films' : pd.read_sql_table('table_region_stats_films', conn)}}
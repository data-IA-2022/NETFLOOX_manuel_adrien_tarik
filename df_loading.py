import pandas as pd
from db_connection import connect_to_db
import yaml

conn = connect_to_db('../config.yaml', 'mysql_azure_netfloox')

datasets = {'tables' : {'films' : pd.read_pickle('./projet_netfloox/dataset_prédiction.pickle')},
            'analyses': {'notes' : pd.read_sql_table('table_distrib_notes', conn),
                         'types' : pd.read_sql_table('table_distrib_types', conn),
                         'films_votes_rating_annee' : pd.read_sql_table('table_list_films_ex', conn),
                         'decenie_votes_rating' : pd.read_sql_table('table_decenie_votes_rating', conn),
                         'prop_notes_null' : pd.read_sql_table('table_prop_notes_null', conn),
                         'region_diffusion_films' : pd.read_sql_table('table_region_len2_diffusion_films', conn),
                         'classement_regions_production_films' : pd.read_sql_table('vue_classement_regions_production_films', conn),
                         'region_len2_stats_films' : pd.read_sql_table('table_region_len2_stats_films', conn),
                         'region_stats_films' : pd.read_sql_table('table_region_stats_films', conn)}}
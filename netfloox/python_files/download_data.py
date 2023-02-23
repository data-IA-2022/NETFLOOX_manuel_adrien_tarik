import requests
import os

url = 'https://datasets.imdbws.com/'

list_files = [
    'name.basics.tsv.gz',
    'title.akas.tsv.gz',
    'title.basics.tsv.gz',
    'title.crew.tsv.gz',
    'title.episode.tsv.gz',
    'title.principals.tsv.gz',
    'title.ratings.tsv.gz'
]

folder_save = 'data'
path_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), folder_save)

for f in list_files:

    print(f"Download '{url + f}' in /{folder_save}/ ... ", end='')

    r = requests.get(url + f)

    path_file = os.path.join(path_folder, f)
    open(path_file, 'wb').write(r.content)

    print("Done")
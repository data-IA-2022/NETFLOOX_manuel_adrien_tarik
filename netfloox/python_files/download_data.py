import requests
from os.path import join
from .utils import relative_path

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
path_folder = relative_path(folder_save)

for f in list_files:

    print(f"Download '{url + f}' in /{folder_save}/ ... ", end='')

    r = requests.get(url + f)

    path_file = join(path_folder, f)
    open(path_file, 'wb').write(r.content)

    print("Done")
import requests

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

for f in list_files:

    print(f"Download '{url + f}' in /{folder_save}/ ... ", end='')

    r = requests.get(url + f)

    open(folder_save + '/' + f, 'wb').write(r.content)

    print("Done")
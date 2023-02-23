from django.shortcuts import render
import pandas as pd

from python_files.model_recommandation import Model_reco
from python_files.analyse import diagrame_3D_numeric_dimentions #Nombre_films_produits_par_regions
from python_files.df_loading import datasets as dts
from plotly.offline import plot


def base(request):

    return render(request, "base.html")


def home(request):

    return render(request, 'home.html')


def analyse(request):

    fig = diagrame_3D_numeric_dimentions(dts['tables']['films'])
    graph = plot(fig, output_type="div")

    return render(request, 'analyse.html', context={"graphique" : graph})


def prediction(request):

    if request.method == 'POST':

        original_title = request.POST.get('originalTitle')
        runtime_minutes = request.POST.get('runtimeMinutes', None)
        is_adult = request.POST.get('isAdult', 0)
        start_year = request.POST.get('startYear', None)
        genres = request.POST.get('genres', '')
        actor = request.POST.get('actor', '')
        actress = request.POST.get('actress', '')
        composer = request.POST.get('composer', '')
        director = request.POST.get('director', '')

        if not original_title:
            error_message = 'You must enter an original title.'
            return render(request, 'prediction.html', {'error_message': error_message})

        # do something with the input data
        df = pd.DataFrame({'originalTitle': original_title,
                            'runtimeMinutes' : runtime_minutes,
                            'isAdult' : is_adult,
                            'startYear' : start_year,
                            'genres' : genres,
                            'actor' : actor,
                            'actress' : actress,
                            'composer' : composer,
                            'director' : director}, index=[0])

        print(df)

        if df.empty:
            error_message = 'The dataframe is empty.'

            return render(request, 'prediction.html', {'error_message': error_message})

        return render(request, 'prediction.html', {'df': df})

    else:

        return render(request, 'prediction.html')



def recomendation(request):

    model = Model_reco(verbose=True)

    # interception d'un méssage POST
    if request.method == "POST":

        print('------------------------------------')
        print(request.POST.get("film"))
        print(request.POST.get("film_but"))
        print('-------------------------------------')

        # Si le message est issu du boutons de recommandation
        if request.POST.get("film_but")=="@//@@///@@@@////":

            df_reco = model.get_reco(request.POST.get("film"), 6)[1:]

            print(df_reco)

            return render(request, "recomendation.html", {"df": df_reco, 'txt_default': request.POST.get("film")})

        # Si le message est issu du champs de saisie de films
        elif request.POST.get("film") != "":

            df = model.noms_films

            options_html = []

            # filtrage des fims en fonction du contenue du champs de saisie
            df_filter = df[df["originalTitle"].fillna("").str.lower().str.contains(request.POST.get("film").lower())]

            print(df_filter.shape[0])

            # S'il y a mois de 600 lignes, la liste de films est envoyer
            if df_filter.shape[0] < 600:

                for option in df[df["originalTitle"].fillna("").str.lower().str.contains(request.POST.get("film").lower())].index:
                    #print(df.iloc[option]["originalTitle"])
                    options_html.append(df.iloc[option]["originalTitle"])

                options_html = sorted(set(options_html))

            return render(request, "recomendation.html", {"test": options_html, 'txt_default': request.POST.get("film")})

    return render(request, "recomendation.html")

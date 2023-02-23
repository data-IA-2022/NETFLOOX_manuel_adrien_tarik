from django.shortcuts import render
from django.db import connections
import pandas as pd
from .models import TableListFilms
from django.http import JsonResponse
from python_files.analyse import Nombre_films_produits_par_regions
from python_files.model_recommandation import Model_reco


def base(request):
    return render(request, "base.html")


def home(request):
    return render(request, 'home.html')


def analyse_(request):
    graph = Nombre_films_produits_par_regions(dts['analyses']['classement_regions_production_films'])  
    return render(request, 'analyse.html', context={"graphique" : graph})


def prediction(request):
    if request.method == 'POST':
        elements = request.POST.getlist('elements[]')
        if not elements:
            error_message = 'You must enter at least one element.'
            return render(request, 'prediction.html', {'error_message': error_message})
        df = pd.DataFrame({'elements': elements})
        # do something with the dataframe
        if df.empty:
            error_message = 'The dataframe is empty.'
            return render(request, 'prediction.html', {'error_message': error_message})
        return render(request, 'prediction.html', {'df': df})
    else:
        return render(request, 'prediction.html')


def recomendation(request):

    model = Model_reco(verbose=True)

    context={}

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

            context = {"df": df_reco}


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
                context = {"test": options_html, 'txt_default': request.POST.get("film")}

            else:
                context = {"test": options_html, 'txt_default': request.POST.get("film")}

    return render(request, "recomendation.html", context)



# def get_films(request):
#     with connections['default'].cursor() as cursor:
#         cursor.execute('SELECT originalTitle FROM table_list_films LIMIT 10')
#         film_list = [element[0] for element in cursor.fetchall()]
#         print(film_list)
#         return film_list

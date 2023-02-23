from django.shortcuts import render
from django.db import connections
from django import forms
import pandas as pd 
import sys
sys.path.append('../')
from .models import TableRegionDiffusionAvgRatingVotesFilms #TableListFilms
from django.http import JsonResponse
from analyse import Diagrame_3D_numeric_dimentions #Nombre_films_produits_par_regions
from df_loading import datasets as dts
from plotly.offline import plot




def base(request):
    return render(request, "base.html")

def home(request):
    return render(request, 'home.html')

def analyse(request):
    fig = Diagrame_3D_numeric_dimentions(dts['tables']['films'])
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








# def prediction(request):
#     if request.method == 'POST':
#         elements = request.POST.getlist('elements[]')
#         if not elements:
#             error_message = 'You must enter at least one element.'
#             return render(request, 'prediction.html', {'error_message': error_message})
#         df = pd.DataFrame({'elements': elements})
#         # do something with the dataframe
#         if df.empty:
#             error_message = 'The dataframe is empty.'
#             return render(request, 'prediction.html', {'error_message': error_message})
#         return render(request, 'prediction.html', {'df': df})
#     else:
#         return render(request, 'prediction.html')



def recomendation(request):
    if request.method == 'GET':
        search_term = request.GET.get('q')
        if search_term:
            with connections['default'].cursor() as cursor:
                cursor.execute("SELECT originalTitle FROM table_list_films WHERE originalTitle LIKE %s LIMIT 10", [f'%{search_term}%'])
                films = [{'id': idx, 'text': row[0]} for idx, row in enumerate(cursor.fetchall())]
        else:
            films = []
        return render(request, 'recomendation.html',dict({'films': films, 'count': len(films)}))
    else:
        film_name = request.POST.get('film_name')
        return render(request, 'netfloox_app/recomendation.html')






# def get_films(request):
#     with connections['default'].cursor() as cursor:
#         cursor.execute('SELECT originalTitle FROM table_list_films LIMIT 10')
#         film_list = [element[0] for element in cursor.fetchall()]
#         print(film_list)
#         return film_list

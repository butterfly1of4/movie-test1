from django.shortcuts import render
from .models import Movie
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .serializers import MovieSerializer
# from .serializers import *
from rest_framework import generics, permissions
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.



class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class= MovieSerializer

    #     all_movies = Movie.objects.all()

# def full_list(request):
#     all_movies = {}
#     if request.method == ' GET':
#         # return render(request)
#         test_titles = request.GET['test_titles']
#         url = 'https://api.nytimes.com/svc/movies/v2/reviews/all.json' % test_titles
#         headers = {"Accept": "application/json"}
#         test_request = request.GET(url, headers)
#         response = requests.get(test_request)
#         data = response.json()

#         movies = data['movies']

#         for i in movies:
#             movie_data = Movie(
#                 display_title=i['display_title'],
#                 byline=i['byline'],
#                 opening_date=i['opening_date'],
#                 headline=i['headline'],
#                 summary_short=i['summary_short'],
#                 url=i['url'],
#                 image=i['src']
#             )
#         movie_data.save()
#         all_movies = Movie.objects.all().order_by('-id')

#     return render(request, 'movie/full_list.html', {'all_movies': all_movies})

    # requestUrl = "https://api.nytimes.com/svc/movies/v2/reviews/all.json?offset=40&api-key=sfbk5jSb84G0nJipPKAKxLvo7hF6tZ3a"
    # requestHeaders = {
    #     "Accept": "application/json"
    # }

    # request = requests.get(requestUrl, headers=requestHeaders)

    # return render(request, 'movie/full_list.html', {'all_movies': all_movies})

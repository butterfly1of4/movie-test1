from django.shortcuts import render
from .models import Movie
# import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import MovieSerializer
# from .serializers import *
from rest_framework import generics, permissions
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated)
# def full_list(request):
#     all_movies= Movie.objects.all()
#     if 'display_title' in request.GET:
#         display_title=request.GET['display_title']
#         url='https://api.nytimes.com/svc/movies/v2/reviews/all.json?offset=20&order=by-opening-date&api-key=sfbk5jSb84G0nJipPKAKxLvo7hF6tZ3a'

#         response= request.get(url)
#         data=response.json()
#         movies= data['movies']

#         for i in movies:
#             movie_data=Movie(
#                 display_title= i['display_title'],
#                 byline = i['byline'],
#                 opening_date = i['opening_date'],
#                 headline = i['headline'],
#                 summary_short =  i['summary_short'],
#                 url= i['url'],
#                 image = i['src']
#             )
#             movie_data.save()
#             all_movies = Movie.objects.all().order_by('-id')
#     return render (request, 'movie/full_list.html', {'all_movies': all_movies})


# THIS RENDERS
# def execute(request):
#     movies = Movie.objects.only()
#     requestUrl = "https://api.nytimes.com/svc/movies/v2/reviews/all.json?offset=40&api-key=sfbk5jSb84G0nJipPKAKxLvo7hF6tZ3a"
#     requestHeaders = {
#         "Accept": "application/json"
#     }

#     new_request = request.GET.get(requestUrl, requestHeaders)
#     return render(request,'movie/full_list.html', {'movies': movies})


# if __name__ == "__main__":
#   execute(new_request)

# @api_view(['GET', 'POST'])
# def full_list(request):
#     all_movies = {}
#     if request.method == 'GET':

#         # requestHeaders = {
#         # "Accept": "application/json"
#         # }
#         test_titles = request.GET['all_movies']
#         requestUrl = "https://api.nytimes.com/svc/movies/v2/reviews/all.json?offset=40&api-key=sfbk5jSb84G0nJipPKAKxLvo7hF6tZ3a" % test_titles
#         # url = 'https://api.nytimes.com/svc/movies/v2/reviews/all.json' % test_titles
#         headers = {"Accept": "application/json"}
#         test_request = request.get(requestUrl, headers)
#         response = requests.get(test_request)
#         data = response.json()
#         request = requests.POST.get(requestUrl, headers=headers)

#     return render(request, 'movie/full_list.html', {'all_movies': all_movies})
    #     data = []
    #     # nextPage = 1
    #     # previousPage = 1
    #     movies = Movie.objects.all()
    #     page = request.GET.get('page', 1)
    #     paginator = Paginator(movies, 10)
    #     try:
    #         data = paginator.page(page)
    #     except PageNotAnInteger:
    #         data = paginator.page(1)
    #     except EmptyPage:
    #         data= paginator.page(paginator.num_pages)

    #     serializer = MovieSerializer(data,context={'request':request}, many=True)
    #     if data.has_next():
    #         next_page = data.next_page_number()
    #     if data.has_previous():
    #         previousPage = data.previous_page_number()

    #         return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/movies/?page=' + str(nextPage), 'prevlink': '/api/moviess/?page=' + str(previousPage)})


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, pk):
#     try:
#         movie = Movie.objects.get(pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = MovieSerializer(movie,context={'request':request})
#         return Response(serializer.data)

# class MovieList(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class= MovieSerializer

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

from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    # path('movies/', views.full_list, name='display_title')
    path('', views.MovieList.as_view(), name='display_title'),
    #NYT
    # path('', views.execute, name='movie_list')
    #OTHER
    # path('', views.get_movies, name='movies')
    #original
    # path('', views.full_list, name='full_list'),
    # path('movies/<int:pk>', views.movie_detail, name='movie_detail')
    # path('/search',)
]
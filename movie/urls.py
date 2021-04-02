from django.urls import path
from . import views


urlpatterns = [
    #NYT
    path('', views.execute, name='movie_list')
    #OTHER
    # path('', views.get_movies, name='movie_list')
    # path('', views.movie_list, name='movie_list'),
    # path('movies/<int:pk>', views.movie_detail, name='movie_detail')
    # path('/search',)
]
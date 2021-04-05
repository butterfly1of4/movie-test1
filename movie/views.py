from django.shortcuts import render
from .models import Movie
import requests
# from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .serializers import MovieSerializer
# from .serializers import *

# from django.urls import reverse_lazy
# from django.views.generic import ListView, DetailView
# from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.


# class MovieList(generics.ListCreateAPIView):
#     queryset = Movies.objects.all()
#     serializer_class= MovieSerializer



from django.shortcuts import render
from django.views.generic import ListView, DetailView

from viewer.models import Movie


class Movies(ListView):
    model = Movie
    template_name = 'movies.html'
    context_object_name = 'movies'


class MovieDetail(DetailView):
    model = Movie
    template_name = 'movie.html'
    context_object_name = 'movie'

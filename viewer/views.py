from django.shortcuts import render
from django.views.generic import ListView

from viewer.models import Movie


class Movies(ListView):
    model = Movie
    template_name = 'movies.html'
    context_object_name = 'movies'

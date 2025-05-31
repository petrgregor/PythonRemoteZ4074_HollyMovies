from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, \
    DeleteView

from viewer.forms import GenreForm, CountryForm, CreatorForm, MovieForm
from viewer.models import Movie, Genre, Country, Creator


class GenreCreateView(CreateView):
    form_class = GenreForm
    template_name = 'form.html'
    success_url = reverse_lazy('movies')

    def form_invalid(self, form):
        print("Formulář 'GenreForm' není validní.")
        return super().form_invalid(form)


class GenreUpdateView(UpdateView):
    form_class = GenreForm
    template_name = 'form.html'
    success_url = reverse_lazy('movies')
    model = Genre

    def form_invalid(self, form):
        print("Formulář 'GenreForm' není validní.")
        return super().form_invalid(form)


class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('movies')


class CountryCreateView(CreateView):
    form_class = CountryForm
    template_name = 'form.html'
    success_url = reverse_lazy('movies')

    def form_invalid(self, form):
        print("Formulář 'CountryForm' není validní.")
        return super().form_invalid(form)


class CountryUpdateView(UpdateView):
    form_class = CountryForm
    template_name = 'form.html'
    success_url = reverse_lazy('movies')
    model = Country

    def form_invalid(self, form):
        print("Formulář 'CountryForm' není validní.")
        return super().form_invalid(form)


class CountryDeleteView(DeleteView):
    model = Country
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('movies')


class CreatorCreateView(CreateView):
    form_class = CreatorForm
    template_name = 'form.html'
    success_url = reverse_lazy('movies')

    def form_invalid(self, form):
        print("Formulář 'CreatorForm' není validní.")
        return super().form_invalid(form)


class CreatorUpdateView(UpdateView):
    form_class = CreatorForm
    template_name = 'form.html'
    success_url = reverse_lazy('movies')
    model = Creator

    def form_invalid(self, form):
        print("Formulář 'CreatorForm' není validní.")
        return super().form_invalid(form)


class CreatorDeleteView(DeleteView):
    model = Creator
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('movies')


class Movies(ListView):
    model = Movie
    template_name = 'movies.html'
    context_object_name = 'movies'


class MovieDetail(DetailView):
    model = Movie
    template_name = 'movie.html'
    context_object_name = 'movie'


class MovieCreate(CreateView):
    form_class = MovieForm
    template_name = 'form.html'
    success_url = reverse_lazy('movies')


class MovieUpdate(UpdateView):
    form_class = MovieForm
    template_name = 'form.html'
    model = Movie
    success_url = reverse_lazy('movies')


class MovieDelete(DeleteView):
    template_name = 'confirm_delete.html'
    model = Movie
    success_url = reverse_lazy('movies')

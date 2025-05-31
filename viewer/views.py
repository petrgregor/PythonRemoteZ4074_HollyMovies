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


def queries(request):
    # všechny filmy
    movies_all = Movie.objects.all()

    # filmy žánru drama
    # .get() vrací jeden záznam dle daných parametrů
    genre_drama = Genre.objects.get(name="Drama")
    # .filter() vrací kolekci všech záznamů, které vyhovují daným kritériím
    movies_drama = Movie.objects.filter(genres=genre_drama)

    # filmy žánru komedie
    #movies_comedy = Movie.objects.filter(genres=Genre.objects.get(name="Komedie"))
    movies_comedy = Movie.objects.filter(genres__name='Komedie')

    # filmy žánru Mysteriózní
    genre_mystery = Genre.objects.get(name='Mysteriózní')

    # všechny žánry a jejich filmy
    genres = Genre.objects.all()

    # všechny země a jejich tvůrci
    countries = Country.objects.all()

    # tvůrci seřazení dle data narození
    #creators = Creator.objects.all().order_by('date_of_birth')
    creators = Creator.objects.all().order_by('-date_of_birth')

    # tvůrci narození v roce 1937
    creators_1937 = Creator.objects.filter(date_of_birth__year=1937)

    # tvůrce narozený v roce 1937
    # creator_1937 = Creator.objects.get(date_of_birth__year=1937) ## nefunguje
    creator_1937 = Creator.objects.filter(date_of_birth__year=1937).first()

    # tvůrci narození jindy než v roce 1937
    creators_1937_ne = Creator.objects.exclude(date_of_birth__year=1937)

    # tvůrci narození po roce 1960
    # __gt -> greather then -> větší než
    creators_after_1960 = Creator.objects.filter(date_of_birth__year__gt=1960)
    ## __gte -> greather then equal -> větší rovno
    ## __lt -> less then -> menší než
    ## __lte -> less then equal -> menší rovno

    # více podmínek
    # tvůrci narození mezi roky 1950 a 1960
    #creators_1950_1960 = Creator.objects.filter(date_of_birth__year__gte=1950).filter(date_of_birth__year__lte=1960)
    creators_1950_1960 = Creator.objects.filter(date_of_birth__year__gte=1950,
                                                date_of_birth__year__lte=1960)

    context = {'movies_all': movies_all,
               'movies_drama': movies_drama,
               'movies_comedy': movies_comedy,
               'genre_mystery': genre_mystery,
               'genres': genres,
               'countries': countries,
               'creators': creators,
               'creators_1937': creators_1937,
               'creator_1937': creator_1937,
               'creators_after_1960': creators_after_1960,
               'creators_1950_1960': creators_1950_1960}
    return render(request=request,
                  template_name='queries.html',
                  context=context)

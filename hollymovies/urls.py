"""
URL configuration for hollymovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from viewer.views import Movies, MovieDetail, GenreCreateView, GenreUpdateView, \
    GenreDeleteView, CountryCreateView, CountryUpdateView, CountryDeleteView, \
    CreatorCreateView, CreatorUpdateView, CreatorDeleteView, MovieCreate, \
    MovieUpdate, MovieDelete, queries

urlpatterns = [
    path('admin/', admin.site.urls),

    path('genre/create/', GenreCreateView.as_view(), name='genre_create'),
    path('genre/update/<int:pk>/', GenreUpdateView.as_view(), name='genre_update'),
    path('genre/delete/<int:pk>/', GenreDeleteView.as_view(), name='genre_delete'),
    path('country/create/', CountryCreateView.as_view(), name='country_create'),
    path('country/update/<int:pk>/', CountryUpdateView.as_view(), name='country_update'),
    path('country/delete/<int:pk>/', CountryDeleteView.as_view(), name='country_delete'),
    path('creator/create/', CreatorCreateView.as_view(), name='creator_create'),
    path('creator/update/<int:pk>/', CreatorUpdateView.as_view(), name='creator_update'),
    path('creator/delete/<int:pk>/', CreatorDeleteView.as_view(), name='creator_delete'),
    path('movies/', Movies.as_view(), name='movies'),
    path('movie/<int:pk>/', MovieDetail.as_view(), name='movie'),
    path('movie/create/', MovieCreate.as_view(), name='movie_create'),
    path('movie/update/<int:pk>/', MovieUpdate.as_view(), name='movie_update'),
    path('movie/delete/<int:pk>/', MovieDelete.as_view(), name='movie_delete'),

    path('queries/', queries, name='queries'),
]

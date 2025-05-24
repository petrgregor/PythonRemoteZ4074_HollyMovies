import datetime

from django.test import TestCase

from viewer.models import Movie, Genre, Country, Creator


class MovieModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        movie = Movie.objects.create(
            title_orig="Originální název filmu",
            title_cz="Český název filmu",
            length=122,
            description="Popis filmu",
            released_date=datetime.date(2001, 2, 3)
        )
        genre1 = Genre.objects.create(name="Drama")
        genre2 = Genre.objects.create(name="Komedie")
        movie.genres.add(genre1)
        movie.genres.add(genre2)
        movie.genres.add(genre1)

        country1 = Country.objects.create(name="Česko")
        country2 = Country.objects.create(name="Slovensko")
        movie.countries.add(country1)
        movie.countries.add(country2)

        director = Creator.objects.create(
            name="Arnošt",
            surname="Novák",
            country=country1,
            date_of_birth=datetime.date(1970, 5, 30),
            biography="Režisér nějakého filmu"
        )
        movie.directors.add(director)

        actor1 = Creator.objects.create(
            name="Bedřich",
            surname="Svoboda",
            country=country1,
            date_of_birth=datetime.date(1985, 5, 20),
            biography="Mizerný herec"
        )
        actor2 = Creator.objects.create(
            name="Ctirad",
            surname="Brzobohatý",
            country=country2,
            date_of_birth=datetime.date(1980, 4, 20),
            biography="Skvělý herec"
        )
        movie.actors.add(actor1)
        movie.actors.add(actor2)

        movie.save()

    def test_title_orig(self):
        movie = Movie.objects.get(id=1)
        self.assertEqual(movie.title_orig, "Originální název filmu")

    def test_length_format(self):
        movie = Movie.objects.get(id=1)
        self.assertEqual(movie.length_format(), "2:02")

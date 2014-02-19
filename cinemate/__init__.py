# coding=utf-8

"""
Реализация API сайта cinemate.cc на языке python.
"""
from .cinemate import Cinemate
from .movie import Movie, Poster, Title, Genre, Country, Rating
from .person import Person, Photo
from .lists import countries, genres
from .version import VERSION


__all__ = (
    'Cinemate',
    'Movie',
    'Person',
    'Poster',
    'Rating',
    'Title',
    'Genre',
    'Country',
    'Photo',
    'countries',
    'genres',
)

__version__ = VERSION

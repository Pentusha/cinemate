from .cinemate import Cinemate
from .movie import Movie, Poster, Title, Genre, Country, Rating
from .person import Person, Photo
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
)

__version__ = VERSION

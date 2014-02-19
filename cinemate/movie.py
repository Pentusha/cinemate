# coding=utf-8
"""
    cinemate.movie
    ~~~~~~~~~~~~~~

    Модуль реализует класс фильма Movie, а также сопутствующие
    Country, Genre, Title, Poster, Release, Rating

"""
from datetime import date, datetime
from six import iteritems
from six.moves import map
from .utils import require, parse_date, BaseCinemate
from .lists import countries, genres


class Country(BaseCinemate):
    """ Страна
        список стран http://cinemate.cc/movie/country/
    """
    def __init__(self, name, slug=None):
        """
        :param name: имя страны на русском языке
        :type name: str
        :param slug: slug страны
        :type slug: str
        """
        self.name = name
        self.slug = slug or self.__class__.slug_by_name(name)

    @classmethod
    def from_dict(cls, dct):
        """ Задать страну фильма из словаря, возвращаемого API
        :param dct: словарь, возвращаемый API
        :type dct: dict
        :return страна
        :rtype: ``Country``
        """
        slug = dct.get('slug')
        name = dct.get('name')
        if not slug:
            slug = cls.slug_by_name(name)
        return cls(name=name, slug=slug)

    @classmethod
    def slug_by_name(cls, name):
        """ Получениу slug страны по её названию на русском языке
        :param name: Имя страны на русском языке
        :return: slug страны
        :rtype: str
        """
        finder = (slug for slug, rus in iteritems(countries) if rus == name)
        return next(finder, None)

    def __unicode__(self):
        return '<Country: {name}>'.format(name=self.slug or self.name)


class Genre(BaseCinemate):
    """ Жанр фильма
        список жанров http://cinemate.cc/movie/genre/
    """
    def __init__(self, name, slug=None):
        """
        :param name: название жанра
        :type name: str
        :param slug: slug жанра
        :type slug: str
        """
        self.name = name
        self.slug = slug or self.__class__.slug_by_name(name)

    @classmethod
    def from_dict(cls, dct):
        """ Задать жанр фильма из словаря, возвращаемого API
        :param dct: словарь, возвращаемый API
        :type dct: dict
        :return жанр
        :rtype: ``Genre``
        """
        return cls(name=dct.get('name'), slug=dct.get('slug'))

    @classmethod
    def slug_by_name(cls, name):
        """ Получениу slug жанра по его названию на русском языке
        :param name: Имя жанра на русском языке
        :return: slug страны
        :rtype: str
        """
        finder = (slug for slug, rus in iteritems(genres) if rus == name)
        return next(finder, None)

    def __unicode__(self):
        return '<Genre: {name}>'.format(name=self.slug or self.name)


class Title(BaseCinemate):
    """ Заголовки фильма на разных языках
    """
    fields = {
        'russian': 'title_russian',
        'original': 'title_original',
        'english': 'title_english',
    }

    def __init__(self, russian='', original='', english=''):
        """
        :param russian: название фильма на русском языке
        :type russian: str
        :param original: нригинальное название фильма
        :type original: str
        :param english: название фильма на английском языке
        :type english: str
        """
        self.russian = russian
        self.original = original
        self.english = english

    @classmethod
    def from_dict(cls, dct):
        """ Задать название фильма из словаря, возвращаемого API
        :param dct: словарь, возвращаемый API
        :type dct: dict
        :return фильм:
        :rtype: ``Movie``
        """
        attrs = {k: dct.get(v) for k, v in iteritems(cls.fields) if v in dct}
        return cls(**attrs)

    def __str__(self):
        return self.original or self.russian


class Poster(BaseCinemate):
    """ Постер фильма
    """
    fields = ('small', 'medium', 'big')

    def __init__(self, small='', medium='', big=''):
        """
        :param small: ссылка на картинку маленького размера
        :type small: str
        :param medium: ссылка на картинку среднего размера
        :type medium: str
        :param big: ссылка на картинку большого размера
        :type big: str
        """
        self.small = small
        self.medium = medium
        self.big = big

    @classmethod
    def from_dict(cls, dct):
        """ Постер фильма из словаря, возвращаемого API
        :param dct: словарь, возвращаемый API
        :type dct: dict
        :return: Дата релиза
        :rtype: Release
        """
        return cls(**{k: dct[k].get('url') for k in cls.fields if k in dct})

    def __unicode__(self):
        sizes = '/'.join(k for k, v in sorted(iteritems(self.__dict__)) if k)
        return '<Poster {sizes}>'.format(sizes=sizes)


class Release(BaseCinemate):
    """ Даты релиза фильма
    """
    fields = {
        'world': 'release_date_world',
        'russia': 'release_date_russia',
    }
    repr_fields = ('world', )
    id_field = 'world'

    def __init__(self, world=None, russia=None):
        """
        :param world: дата релиза в Мире
        :type: str
        :param russia: дата релиза в России
        :type: str
        """
        self.world = parse_date(world)
        self.russia = parse_date(russia)

    def __unicode__(self):
        fields = '/'.join(k for k, v in sorted(iteritems(self.__dict__)) if k)
        return '<Release {fields}>'.format(fields=fields)


class Rating(BaseCinemate):
    """ Рейтинг фильма imdb и kinopoisk
    """
    repr_fields = ('rating', 'votes',)
    id_field = 'rating'

    def __init__(self, votes=0, rating=0):
        """
        :param votes:
        :type votes:
        :param rating:
        :type rating:
        """
        self.votes = int(votes)
        self.rating = float(rating)

    def __unicode__(self):
        return '<Rating rating={rating:.1f} votes={votes}>'.format(
            rating=self.rating,
            votes=self.votes
        )


class Movie(BaseCinemate):
    """ Класс фильма
    """

    fields = (
        'type', 'title', 'year', 'poster', 'description', 'runtime', 'release',
        'imdb', 'kinopoisk', 'country', 'genre', 'director', 'cast', 'trailer',
        'url',
    )

    def __init__(self, movie_id, **kwargs):
        """
        :param movie_id: Идентификатор фильма на cinemate.cc
        :type movie_id: int
        """
        self.id = movie_id
        self.title = Title()
        for field in self.__class__.fields:
            value = kwargs.get(field)
            if value:
                setattr(self, field, value)

    @classmethod
    def from_dict(cls, dct):
        """ Получить информацию о фильме из словаря, возвращаемого API
        :param dct: словарь, возвращаемый API
        :type dct: dict
        :return: Фильм
        :rtype: Movie
        """
        movie_id = int(dct['url'].split('/')[-2])
        cinemate = getattr(cls, 'cinemate')
        cast = dct.get('cast', {}).get('person', [])
        director = dct.get('director', {}).get('person', [])
        release = Release(
            dct.get('release_date_world'),
            dct.get('release_date_russia')
        )
        genre = dct.get('genre', [])
        country = dct.get('country', [])
        if isinstance(cast, dict):
            cast = (cast, )
        if isinstance(director, dict):
            director = (director, )
        if isinstance(genre, dict):
            genre = (genre, )
        if isinstance(country, dict):
            country = (country, )
        return cls(
            movie_id,
            title=Title.from_dict(dct),
            year=dct.get('year'),
            type=dct.get('type'),
            description=dct.get('description'),
            imdb=Rating(**dct.get('imdb', {})),
            kinopoisk=Rating(**dct.get('kinopoisk', {})),
            poster=Poster.from_dict(dct.get('poster', {})),
            release=release,
            runtime=dct.get('runtime'),
            trailer=dct.get('trailer'),
            url=dct.get('url'),
            genre=list(map(Genre.from_dict, genre)),
            country=list(map(Country.from_dict, country)),
            cast=list(map(cinemate.person.from_dict, cast)),
            director=list(map(cinemate.person.from_dict, director)),
        )

    @classmethod
    @require('apikey')
    def get(cls, movie_id):
        """ Короткий аналог movie(123).fetch()
        :param movie_id: Идентификатор требуемого фильма
        :type movie_id: int
        :return: Фильм
        :rtype: Movie
        """
        return cls(movie_id).fetch()

    @require('apikey')
    def fetch(self):
        """ Получить полную информацию о фильме
            http://cinemate.cc/help/api/movie/
        :return: фильм
        :rtype: Movie
        """
        url = 'movie'
        cinemate = getattr(self, 'cinemate')
        params = {'id': self.id}
        req = cinemate.api_get(url, apikey=True, params=params)
        movie = req.json().get('movie')
        return cinemate.movie.from_dict(movie)

    @classmethod
    @require('apikey')
    def search(cls, term):
        """ Поиск по заголовкам фильмов.
            Поддерживается уточняющий поиск по году выхода фильма и
            коррекцию ошибок при печати
            http://cinemate.cc/help/api/movie.search/
        :param term: искомая строка
        :type term: str
        :return: список фильов
        :rtype: list
        """
        url = 'movie.search'
        cinemate = getattr(cls, 'cinemate')
        params = {'term': term}
        req = cinemate.api_get(url, apikey=True, params=params)
        movies = req.json().get('movie', [])
        return list(map(cls.from_dict, movies))

    @classmethod
    @require('apikey')
    def list(cls, **kwargs):
        """ Результаты поиска фильмов, используя заданные фильтры.
            Возвращается 10 первых фильмов
            http://cinemate.cc/help/api/movie.list/
        :param kwargs: именованные фильтры
        :type kwargs: dict
        :param type: тип фильмов. Возможные значения: movie, serial, short
        :type type: str
        :param year: год выпуска фильма или сериала
        :type year: int
        :param genre: slug жанра http://cinemate.cc/movie/genre/
        :type genre: str or ``cinemate.Genre``
        :param country: slug страны http://cinemate.cc/movie/country/
        :type country: str or ``cinemate.Country``
        :param order_by: критерий сортировки:
                         create_date, release_date, ru_release_date
        :type order_by: str
        :param order: порядок сортировки параметра order_by: desc, asc
        :type order: str
        :param order_from: начальная дата среза параметра ``order_by``
            в формате ДД.ММ.ГГГГ
        :type order_from: datetime.date or str
        :param order_to: конечная дата среза параметра ``order_by``
            в формате ДД.ММ.ГГГГ
        :type order_to: datetime.date or str
        :param page: страница в выборке (по умолчанию 0)
        :type page: int
        :param per_page: записей в выборке (по умолчанию 10, максимум 25)
        :type per_page: int
        :return: Список фильмов
        :rtype: list
        :raises ValueError: вызывается если указан один из параметров
            ``order_to``/``order_from``, но не указан ``order_by``
        """
        country = kwargs.get('country')
        genre = kwargs.get('genre')
        order_by = kwargs.get('order_by')
        order_from = kwargs.get('order_from')
        order_to = kwargs.get('order_to')
        if isinstance(order_from, (date, datetime)):
            order_from = order_from.strftime('%d.%m.%Y')
        if isinstance(order_to, (date, datetime)):
            order_to = order_to.strftime('%d.%m.%Y')
        if (order_to or order_from) and not order_by:
            msg = (
                'You must specify order_by parameter '
                'if you are using order_to or order_from'
            )
            raise ValueError(msg)
        params = {
            'year': kwargs.get('year'),
            'genre': genre or getattr(genre, 'slug', None),
            'country': country or getattr(country, 'slug', None),
            'order_by': order_by,
            'order': kwargs.get('order'),
            'from': order_from,
            'to': order_to,
            'page': kwargs.get('page'),
            'per_page': kwargs.get('per_page'),
        }
        url = 'movie.list'
        cinemate = getattr(cls, 'cinemate')
        params = {k: v for k, v in iteritems(params) if v is not None}
        req = cinemate.api_get(url, apikey=True, params=params)
        movies = req.json().get('movie')
        return list(map(cls.from_dict, movies))

    def __unicode__(self):
        fields = str(self.id), self.title.original or self.title.russian
        fields = ' '.join(fields)
        return '<Movie {fields}>'.format(fields=fields)

# coding=utf-8
"""
    Модуль реализует класс фильма Movie, а также сопутствующие
    Country, Genre, Title, Poster, Release, Rating.
"""
from datetime import date, datetime
from six import iteritems
from six.moves import map
from .lists import countries, genres
from .utils import (require, parse_date, BaseCinemate, BaseImage, BaseSlug,
                    CompareMixin, FieldsCompareMixin)


class Country(BaseSlug):
    """ `Страна <http://cinemate.cc/movie/country/>`_ производства фильма.

    :param name: имя страны на русском языке
    :type name: :py:class:`str`
    :param slug: slug страны
    :type slug: :py:class:`str`
    """
    mapping = countries


class Genre(BaseSlug):
    """ `Жанр фильма <http://cinemate.cc/movie/genre/>`_.

    :param name: название жанра
    :type name: :py:class:`str`
    :param slug: slug жанра
    :type slug: :py:class:`str`
    """
    mapping = genres


class Title(FieldsCompareMixin, BaseCinemate):
    """ Заголовки фильма на разных языках.

    :param russian: название фильма на русском языке
    :type russian: :py:class:`str`
    :param original: оригинальное название фильма
    :type original: :py:class:`str`
    :param english: название фильма на английском языке
    :type english: :py:class:`str`
    """
    fields = {
        'russian': 'title_russian',
        'original': 'title_original',
        'english': 'title_english',
    }

    def __init__(self, russian='', original='', english=''):
        self.russian = russian
        self.original = original
        self.english = english

    @classmethod
    def from_dict(cls, dct):
        """ Задать название фильма из словаря, возвращаемого API.

        :param dct: словарь, возвращаемый API
        :type dct: :py:class:`dict`
        :return: фильм
        :rtype: ``.Movie``
        """
        attrs = {k: dct.get(v) for k, v in iteritems(cls.fields) if v in dct}
        return cls(**attrs)

    def __unicode__(self):
        return self.original or self.russian or ''


class Poster(BaseImage):
    """ Постер фильма в трёх размерах.

    :param small: ссылка на картинку маленького размера
    :type small: :py:class:`str`
    :param medium: ссылка на картинку среднего размера
    :type medium: :py:class:`str`
    :param big: ссылка на картинку большого размера
    :type big: :py:class:`str`
    """


class Release(FieldsCompareMixin, BaseCinemate):
    """ Даты релиза фильма.

    :param world: дата выхода фильма в прокат
    :type world: :py:class:`str`
    :param russia: дата выхода фильма в российский прокат
    :type russia: :py:class:`str`
    """
    fields = 'world', 'russia'

    def __init__(self, world=None, russia=None):
        self.world = parse_date(world)
        self.russia = parse_date(russia)

    def __unicode__(self):
        fields = '/'.join(k for k, v in sorted(iteritems(self.__dict__)) if v)
        return '<Release {fields}>'.format(fields=fields)


class Rating(FieldsCompareMixin, BaseCinemate):
    """ Рейтинг фильма imdb и kinopoisk.

    :param votes: количесвто отданных голосов
    :type votes: :py:class:`int`
    :param rating: рейтинг фильма
    :type rating: :py:class:`float`
    """
    fields = 'votes', 'rating'

    def __init__(self, votes=0, rating=0):
        self.votes = int(votes)
        self.rating = float(rating)

    def __unicode__(self):
        return '<Rating rating={rating:.1f} votes={votes}>'.format(
            rating=self.rating,
            votes=self.votes
        )


class Movie(CompareMixin, BaseCinemate):
    """ Класс реализуюзий фильмы, сериалы, короткометражки.

    :param movie_id: идентификатор фильма на cinemate.cc
    :type movie_id: :py:class:`int`
    :param title: название
    :type title: :class:`.Title`
    :param year: год выхода
    :type year: :py:class:`int`
    :param type: тип ``movie``, ``serial``, ``short``
    :type type: :py:class:`int`
    :param description: описание
    :type description: :py:class:`str`
    :param imdb: рейтинг IMDb
    :type imdb: :class:`.Rating`
    :param kinopoisk: рейтинг kinopoisk
    :type kinopoisk: :class:`.Rating`
    :param poster: постер фильма
    :type poster: :class:`.Poster`
    :param release: даты релиза
    :type release: :class:`.Release`
    :param runtime: продолжительность в минутах
    :type runtime: :py:class:`int`
    :param trailer: ссылка на трейлер
    :type trailer: :py:class:`str`
    :param url: ссылка на cinemate.cc
    :type url: :py:class:`str`
    :param genre: список жанров
    :type genre: :class:`.Genre`
    :param country: список стран
    :type country: :class:`.Country`
    :param cast: список актёров
    :type cast: :py:class:`list`
    :param director: список режиссеров
    :type director: :py:class:`list`
    """

    fields = (
        'type', 'title', 'year', 'poster', 'description', 'runtime', 'release',
        'imdb', 'kinopoisk', 'country', 'genre', 'director', 'cast', 'trailer',
        'url',
    )
    cinemate = None

    def __init__(self, movie_id, **kwargs):
        """ При инициализации принимает все именованные аргументы и делает их
        аттрибутами экземпляра класса.
        """
        self.id = int(movie_id)
        self.title = Title()
        for field in self.fields:
            value = kwargs.get(field)
            if value:
                setattr(self, field, value)

    @classmethod
    def from_dict(cls, dct):
        """ Получить информацию о фильме из словаря, возвращаемого API.

        :param dct: словарь, возвращаемый API
        :type dct: :py:class:`dict`
        :return: фильм
        :rtype: :class:`.Movie`
        """
        movie_id = int(dct['url'].split('/')[-2])
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
            cast=list(map(cls.cinemate.person.from_dict, cast)),
            director=list(map(cls.cinemate.person.from_dict, director)),
        )

    @classmethod
    @require('apikey')
    def get(cls, movie_id):
        """ Короткий аналог movie(123).fetch()

        :param movie_id: идентификатор требуемого фильма
        :type movie_id: :py:class:`int`
        :return: фильм
        :rtype: :class:`.Movie`
        """
        return cls(movie_id).fetch()

    @require('apikey')
    def fetch(self):
        """ Метод API `movie <http://cinemate.cc/help/api/movie/>`_
        получает полную информацию о фильме.

        :return: фильм
        :rtype: :class:`.Movie`
        """
        url = 'movie'
        params = {'id': self.id}
        req = self.cinemate.api_get(url, apikey=True, params=params)
        movie = req.json().get('movie', {})
        return self.cinemate.movie.from_dict(movie)

    @classmethod
    @require('apikey')
    def search(cls, term):
        """ Метод API
        `movie.search <http://cinemate.cc/help/api/movie.search/>`_
        производит поиск по заголовкам фильмов.
        Поддерживается уточняющий поиск по году выхода фильма и
        коррекцию ошибок при печати.

        :param term: искомая строка
        :type term: :py:class:`str`
        :return: список фильов
        :rtype: :py:class:`list`
        """
        url = 'movie.search'
        params = {'term': term}
        req = cls.cinemate.api_get(url, apikey=True, params=params)
        movies = req.json().get('movie', [])
        return list(map(cls.from_dict, movies))

    # noinspection PyDocstring
    @classmethod
    @require('apikey')
    def list(cls, **kwargs):
        """ Метод API `movie.list <http://cinemate.cc/help/api/movie.list/>`_
        возращает результаты поиска фильмов, используя заданные фильтры.
        По-умолчанию возвращается 10 первых фильмов.

        :param kwargs: именованные фильтры
        :type kwargs: :py:class:`dict`
        :param type: тип фильмов. Возможные значения:
            ``movie``, ``serial``, ``short``
        :type type: :py:class:`str`
        :param year: год выпуска фильма или сериала
        :type year: :py:class:`int`
        :param genre: `slug жанра <http://cinemate.cc/movie/genre/>`_
        :type genre: :py:class:`str` or :class:`cinemate.Genre`
        :param country: `slug страны <http://cinemate.cc/movie/country/>`_
        :type country: :py:class:`str` or :class:`cinemate.Country`
        :param order_by: критерий сортировки:
            ``create_date``, ``release_date``, ``ru_release_date``
        :type order_by: :py:class:`str`
        :param order: порядок сортировки параметра ``order_by``:
            ``desc``, ``asc``
        :type order: :py:class:`str`
        :param order_from: начальная дата среза параметра ``order_by``
            в формате ``ДД.ММ.ГГГГ``
        :type order_from: :py:class:`datetime.date` or :py:class:`str`
        :param order_to: конечная дата среза параметра ``order_by``
            в формате ``ДД.ММ.ГГГГ``
        :type order_to: :py:class:`datetime.date` or :py:class:`str`
        :param page: страница в выборке (по умолчанию 0)
        :type page: :py:class:`int`
        :param per_page: количество записей в выборке
            (по умолчанию 10, максимум 25)
        :type per_page: :py:class:`int`
        :return: список фильмов
        :rtype: :py:class:`list`
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
        params = {k: v for k, v in iteritems(params) if v is not None}
        req = cls.cinemate.api_get(url, apikey=True, params=params)
        movies = req.json().get('movie', [])
        return list(map(cls.from_dict, movies))

    def __unicode__(self):
        fields = str(self.id), self.title.original or self.title.russian
        fields = ' '.join(fields)
        return '<Movie {fields}>'.format(fields=fields)

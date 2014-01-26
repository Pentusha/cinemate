# coding=utf-8
from six import iteritems, PY2
from six.moves import map
from .utils import require, parse_date, BaseCinemate


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
        self.slug = slug

    @classmethod
    def from_dict(cls, dct):
        """ Задать страну фильма из словаря, возвращаемого API
        :param dct: словарь, возвращаемый API
        :type dct: dict
        :return страна
        :rtype: ``Country``
        """
        return cls(name=dct.get('name'), slug=dct.get('slug'))

    def __str__(self):
        name = self.slug or self.name
        if PY2:
            name = name.encode('utf-8')
        return '<Country: {name}>'.format(name=name)


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
        self.slug = slug

    @classmethod
    def from_dict(cls, dct):
        """ Задать жанр фильма из словаря, возвращаемого API
        :param dct: словарь, возвращаемый API
        :type dct: dict
        :return жанр
        :rtype: ``Genre``
        """
        return cls(name=dct.get('name'), slug=dct.get('slug'))

    def __str__(self):
        name = self.slug or self.name
        if PY2:
            name = name.encode('utf-8')
        return '<Genre: {name}>'.format(name=name)


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
        attrs = dict((k, dct.get(v))
                     for k, v in iteritems(cls.fields) if v in dct)
        return cls(**attrs)

    def __str__(self):
        name = self.russian
        if PY2:
            name = name.encode('UTF-8')
        return name


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
        return cls(**dict((k, dct[k].get('url'))
                          for k in cls.fields if k in dct))

    def __str__(self):
        sizes = '/'.join(k for k, v in iteritems(self.__dict__) if k)
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

    @classmethod
    def from_dict(cls, dct):
        """ Дата релиза из словаря, возвращаемого API
        :param dct: словарь, возвращаемый API
        :type dct: dict
        :return: Дата релиза
        :rtype: Release
        """
        attrs = dict((k, dct.get(v))
                     for k, v in cls.fields.items() if v in dct)
        return cls(**attrs)

    def __str__(self):
        fields = '/'.join(k for k, v in iteritems(self.__dict__) if k)
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

    def __str__(self):
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
    repr_fields = ('id', 'title', 'year',)
    id_field = 'id'

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
        genres = dct.get('genre', [])
        countries = dct.get('country', [])
        if isinstance(cast, dict):
            cast = (cast, )
        if isinstance(director, dict):
            director = (director, )
        if isinstance(genres, dict):
            genres = (genres, )
        if isinstance(countries, dict):
            countries = (countries, )
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
            genre=list(map(Genre.from_dict, genres)),
            country=list(map(Country.from_dict, countries)),
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
    def search(cls, term, year=None):
        """ Поиск по заголовкам фильмов.
            Поддерживается уточняющий поиск по году выхода фильма и
            коррекцию ошибок при печати
            http://cinemate.cc/help/api/movie.search/
        :param term: искомая строка
        :type term: str
        :param year: год выхода фильма
        :type year: int
        :return: список фильов
        :rtype: list
        """
        url = 'movie.search'
        cinemate = getattr(cls, 'cinemate')
        if year is not None:
            term = '{term} {year}'.format(term=term, year=year)
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
        :param type: тип фильмов. Возможные значения: movie, serial, short
        :type type: str
        :param year: год выпуска фильма или сериала
        :type year: int
        :param genre: slug жанра http://cinemate.cc/movie/genre/
        :type genre: str
        :param country: slug страны http://cinemate.cc/movie/country/
        :type country: str
        :param order_by: критерий сортировки:
                         create_date, release_date, ru_release_date
        :type order_by: str
        :param order: порядок сортировки параметра order_by: desc, asc
        :type order: str
        :param order_from: начальная дата среза параметра order_by
        :type order_from: datetime.date
        :param order_to: конечная дата среза параметра order_by
        :type order_to: datetime.date
        :param page: страница в выборке (по умолчанию 0)
        :type page: int
        :param per_page: записей в выборке (по умолчанию 10, максимум 25)
        :type per_page: ints
        :return: Список фильмов
        :rtype: list
        """
        url = 'movie.list'
        cinemate = getattr(cls, 'cinemate')
        params = {
            'year': kwargs.get('year'),
            'genre': kwargs.get('genre'),
            'country': kwargs.get('country'),
            'order_by': kwargs.get('order_by'),
            'order': kwargs.get('order'),
            'from': kwargs.get('order_from'),
            'to': kwargs.get('order_to'),
            'page': kwargs.get('page'),
            'per_page': kwargs.get('per_page'),
        }
        params = dict((k, v) for k, v in iteritems(params) if v is not None)
        req = cinemate.api_get(url, apikey=True, params=params)
        movies = req.json().get('movie')
        return list(map(cls.from_dict, movies))

    def __str__(self):
        fields = [str(self.id)]
        if self.title.russian:
            fields.append(self.title.russian)
        fields = ' '.join(fields)
        if PY2:
            fields = fields.encode('utf-8')
        return '<Movie {fields}>'.format(fields=fields)



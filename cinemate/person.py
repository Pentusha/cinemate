# coding=utf-8
"""
    cinemate.person
    ~~~~~~~~~~~~~~~

    Модуль реализует класс персоны Person,
    а также класс фотографии персоны Photo

"""
from six import iteritems
from .utils import require, BaseCinemate


class Photo(BaseCinemate):
    """ Фото персоны
    """
    fields = ('small', 'medium', 'big')

    def __init__(self, small, medium, big):
        self.small = small
        self.medium = medium
        self.big = big

    @classmethod
    def from_dict(cls, dct):
        """ Фотография персоны из словаря, возвращаемого API
        :param dct: словарь, возвращаемый API
        :type dct: dict
        :return: Фотография
        :rtype: Photo
        """
        if dct is None:
            return
        fields = {k: dct.get(k).get('url') for k in cls.fields if k in dct}
        return cls(**fields)

    def __unicode__(self):
        sizes = '/'.join(k for k, v in sorted(iteritems(self.__dict__)) if k)
        return '<Photo {sizes}>'.format(sizes=sizes)


class Person(BaseCinemate):
    """ Класс персоны
    """
    def __init__(self, person_id, **kwargs):
        """
        :param person_id: Идентификатор персоны на cinemate.cc
        :type person_id: int
        """
        self.id = person_id
        self.name = kwargs.get('name')
        self.name_original = kwargs.get('name_original')
        self.photo = kwargs.get('photo')
        self.url = kwargs.get('url')

    @classmethod
    def from_dict(cls, dct):
        """ Информация о персоне из словаря, возвращаемого API
        :param dct: словарь, возвращаемый API
        :type dct: dict
        :return: Персона
        :rtype: Person
        """
        return cls(
            person_id=dct.get('id') or dct.get('attrib').get('id'),
            name=dct.get('name') or dct.get('value'),
            name_original=dct.get('name_original'),
            photo=Photo.from_dict(dct.get('photo')),
            url=dct.get('url')
        )

    @require('apikey')
    def fetch(self):
        """ Получение полной информации о персоне
            http://cinemate.cc/help/api/person/
        :return: персона
        :rtype: Person
        """
        url = 'person'
        cinemate = getattr(self, 'cinemate')
        params = {'id': self.id}
        req = cinemate.api_get(url, apikey=True, params=params)
        person = req.json().get('person')
        return cinemate.person.from_dict(person)

    @classmethod
    @require('apikey')
    def get(cls, person_id):
        """ Короткий аналог person(123).fetch()
        :param person_id: идентификатор персоны
        :type person_id: int
        :return: персона
        :rtype: Person
        """
        return cls(person_id).fetch()

    @require('apikey')
    def movies(self):
        """ Фильмы, в съемке которых персона принимала участие в качестве
            актера или режиссера
            http://cinemate.cc/help/api/person.movies/
            :return: словарь с ключачи actor, director
            :rtype: dict
        """
        url = 'person.movies'
        cinemate = getattr(self, 'cinemate')
        params = {'id': self.id}
        req = cinemate.api_get(url, apikey=True, params=params)
        movies = req.json().get('person').get('movies', {})
        actor = movies.get('actor', {}).get('movie', [])
        director = movies.get('director', {}).get('movie', [])
        return {
            'actor': list(map(cinemate.movie.from_dict, actor)),
            'director': list(map(cinemate.movie.from_dict, director)),
        }

    @classmethod
    @require('apikey')
    def search(cls, term):
        """ Метод возвращает первые 10 результатов поиска по базе персон
            http://cinemate.cc/help/api/movie.search/
        :param term: искомая строка; поддерживает коррекцию ошибок при печати
        :type term: str
        :return:  список персон
        :rtype: list
        """
        url = 'person.search'
        cinemate = getattr(cls, 'cinemate')
        params = {'term': term}
        req = cinemate.api_get(url, apikey=True, params=params)
        persons = req.json().get('person', [])
        return list(map(cls.from_dict, persons))

    def __unicode__(self):
        fields = str(self.id), self.name_original or self.name
        fields = ' '.join(fields)
        return '<Person {fields}>'.format(fields=fields)


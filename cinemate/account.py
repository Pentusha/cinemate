# coding=utf-8
"""
    Модуль реализует класс Account для получения пользовательской информации.
"""
from .utils import BaseCinemate, require, parse_datetime
from .movie import Title


class Account(BaseCinemate):
    """ Класс для получения пользовательских данных.
    """
    cinemate = None

    @require('username', 'password')
    def auth(self):
        """ Метод API
        `account.auth <http://cinemate.cc/help/api/account.auth/>`_ возвращает
        passkey.

        :return: passkey
        :rtype: :py:class:`str`
        """
        params = {
            'username': self.cinemate.username,
            'password': self.cinemate.password,
        }
        req = self.cinemate.api_get('account.auth', params=params)
        self.cinemate.passkey = req.json().get('passkey')
        return self.cinemate.passkey

    @require('passkey')
    def profile(self):
        """ Метод API
        `account.profile <http://cinemate.cc/help/api/account.profile/>`_
        получить поля профиля.

        :return: словарь с полями профиля
        :rtype: :py:class:`dict`
        """
        url = 'account.profile'
        req = self.cinemate.api_get(url, passkey=True)
        return req.json()

    @require('passkey')
    def updatelist(self):
        """ Метод API
        `account.updatelist <http://cinemate.cc/help/api/account.updatelist/>`_
        возвращает записи ленты обновлений пользователя.

        :return: список персон и фильмов за которыми следит пользователь
        :rtype: :py:class:`list`
        """
        url = 'account.updatelist'
        req = self.cinemate.api_get(url, passkey=True)
        results = req.json().get('item', [])
        for a in results:
            item = a.get('for_object', {})
            a['date'] = parse_datetime(a['date'])
            if 'person' in item:
                person = item['person']
                person_id = person['id']
                title = person['title']
                person = self.cinemate.person(person_id, name=title)
                a['for_object'] = person
            if 'movie' in item:
                movie = item['movie']
                title, year = movie['title'].rsplit(' ', 1)
                year = int(year.lstrip('(').rstrip(')'))
                movie = self.cinemate.movie(
                    movie['id'],
                    title=title,
                    year=year
                )
                a['for_object'] = movie
        return results

    @require('passkey')
    def watchlist(self):
        """ Метод API
        `account.watchlist <http://cinemate.cc/help/api/account.watchlist/>`_
        возвращает список объектов слежения пользователя.

        :return: словарь объектов слежения с ключами movie, person
        :rtype: :py:class:`dict`
        """
        url = 'account.watchlist'
        req = self.cinemate.api_get(url, passkey=True)
        json_movies = req.json().get('movie', [])
        json_persons = req.json().get('person', [])
        movies = []
        persons = []
        for m in json_movies:
            movie_id = m.get('id', m['url'].split('/')[-2])
            title, year = m['name'].rsplit(' ', 1)
            year = int(year.lstrip('(').rstrip(')'))
            movie = self.cinemate.movie(
                movie_id,
                title=Title(title),
                year=year
            )
            movie.url = m['url']
            movie.date = parse_datetime(m['date'])
            movies.append(movie)
        for p in json_persons:
            person_id = p.get('id', p['url'].split('/')[-2])
            person = self.cinemate.person(person_id, name=p['name'])
            person.url = p['url']
            person.date = parse_datetime(p['date'])
            persons.append(person)
        return {
            'movie': movies,
            'person': persons,
        }

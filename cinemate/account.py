# coding=utf-8
"""
    cinemate.account
    ~~~~~~~~~~~~~~~~

    Модуль реализует класс Account для получения пользовательской информации.

"""
from .utils import BaseCinemate, require, parse_datetime
from .movie import Title


class Account(BaseCinemate):
    """ Класс для получения пользовательских данных
    """
    @require('username', 'password')
    def auth(self):
        """ Получить passkey
            http://cinemate.cc/help/api/account.auth/
        :return: Passkey
        :rtype: str
        """
        cinemate = getattr(self, 'cinemate')
        params = {
            'username': cinemate.username,
            'password': cinemate.password,
        }
        req = cinemate.api_get('account.auth', params=params)
        cinemate.passkey = req.json().get('passkey')
        return cinemate.passkey

    @require('passkey')
    def profile(self):
        """ Получить поля профиля
            http://cinemate.cc/help/api/account.profile/
        :return: Словарь с полями профиля
        :rtype: dict
        """
        url = 'account.profile'
        cinemate = getattr(self, 'cinemate')
        req = cinemate.api_get(url, passkey=True)
        return req.json()

    @require('passkey')
    def updatelist(self):
        """ Записи ленты обновлений пользователя
            http://cinemate.cc/help/api/account.updatelist/
        :return: Список персон, и фильмов за которыми следит пользователь
        :rtype: list
        """
        url = 'account.updatelist'
        cinemate = getattr(self, 'cinemate')
        req = cinemate.api_get(url, passkey=True)
        results = req.json().get('item', [])
        for a in results:
            item = a.get('for_object', {})
            a['date'] = parse_datetime(a['date'])
            if 'person' in item:
                person = item['person']
                person_id = person['id']
                title = person['title']
                person = cinemate.person(person_id, name=title)
                a['for_object'] = person
            if 'movie' in item:
                movie = item['movie']
                title, year = movie['title'].rsplit(' ', 1)
                year = int(year.lstrip('(').rstrip(')'))
                movie = cinemate.movie(movie['id'], title=title, year=year)
                a['for_object'] = movie
        return results

    @require('passkey')
    def watchlist(self):
        """ Метод возвращает список объектов слежения пользователя
            http://cinemate.cc/help/api/account.watchlist/
        :return: словарь объектов слежения с ключами movie, person
        :rtype: dict
        """
        url = 'account.watchlist'
        cinemate = getattr(self, 'cinemate')
        req = cinemate.api_get(url, passkey=True)
        json_movies = req.json().get('movie', [])
        json_persons = req.json().get('person', [])
        movies = []
        persons = []
        for m in json_movies:
            movie_id = m.get('id', m['url'].split('/')[-2])
            title, year = m['name'].rsplit(' ', 1)
            year = int(year.lstrip('(').rstrip(')'))
            movie = cinemate.movie(movie_id, title=Title(title), year=year)
            movie.url = m['url']
            movie.date = parse_datetime(m['date'])
            movies.append(movie)
        for p in json_persons:
            person_id = p.get('id', p['url'].split('/')[-2])
            person = cinemate.person(person_id, name=p['name'])
            person.url = p['url']
            person.date = parse_datetime(p['date'])
            persons.append(person)
        return {
            'movie': movies,
            'person': persons,
        }

# coding=utf-8

from requests import get as http_get
from requests.status_codes import codes
from .utils import BaseCinemate
from .account import Account
from .movie import Movie
from .person import Person
from .stats import Stats


class Cinemate(BaseCinemate):
    base_url = 'http://api.cinemate.cc/'

    def __init__(self, username, password, passkey, apikey):
        """ Инициация главного класса, все остальные создаются внутри.
        :param username: Имя пользователя
        :type username: str
        :param password: Пароль пользователя
        :type password: str
        :param passkey: Получается здесь http://cinemate.cc/preferences/#api
        :type passkey: str
        :param apikey: Получается здесть a@cinemate.cc
        :type apikey: str
        """
        self.username = username
        self.password = password
        self.passkey = passkey
        self.apikey = apikey
        self.movie = type('Movie', (Movie,), {'cinemate': self})
        self.stats = type('Stats', (Stats,), {'cinemate': self})()
        self.person = type('Person', (Person,), {'cinemate': self})
        self.account = type('Account', (Account,), {'cinemate': self})()

    def api_get(self, url, passkey=False, apikey=False, **kwargs):
        """ Получить фтраницу api или сайта
        :param url: адрес получаемой страницы, полностью или p/a/th?param=1
        :type url: str
        :param passkey: Использовать для запроса passkey
        :type passkey: bool
        :param apikey: Использовать для запроса apikey
        :type apikey: bool
        :return: ответ на запрос
        :raises: RuntimeError
        """
        full_url = url.startswith('http://')
        url = full_url and url or self.base_url + url.lstrip('/')
        params = kwargs.pop('params', {})
        params['format'] = 'json'
        if passkey:
            params['passkey'] = self.passkey
        if apikey:
            params['apikey'] = self.apikey
        req = http_get(url, params=params, **kwargs)
        if req.status_code != codes.ok:
            msg = 'cinemate return invalid status code {code} for {url}'
            raise RuntimeError(msg.format(code=req.status_code, url=req.url))
        error = req.json().get('error')
        if error:
            raise RuntimeError(error)
        return req

    def __str__(self):
        return '<Cinemate: {username}>'.format(username=self.username)

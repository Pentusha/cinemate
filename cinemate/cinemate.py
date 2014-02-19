# coding=utf-8
"""
    cinemate.cinemate
    ~~~~~~~~~~~~~~~~~

    Модуль реализует класс Cinemate для хранения пользовательских данных.

"""
from requests import get as http_get
from requests.status_codes import codes
from .utils import BaseCinemate
from .account import Account
from .movie import Movie
from .person import Person
from .stats import Stats


class Cinemate(BaseCinemate):
    """ Класс для хранения пользовательских настроек, таких как
        имя пользователя, пароль, passkey, apikey.
    """
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
        """ Получить страницу api или сайта
        :param url: адрес получаемой страницы, полностью или p/a/th?param=1
        :type url: str
        :param passkey: использовать для запроса passkey
        :type passkey: bool
        :param apikey: использовать для запроса apikey
        :param kwargs: остальные параметры отправляемые в requests.get
        :type apikey: bool
        :return: ответ на запрос
        :raises RuntimeError: вызывается в если в ответе приходит блок error
            или если запрос возвращает некорректный http-статус
        """
        full_url = url.startswith('http://')
        url = full_url and url or self.base_url + url.lstrip('/')
        params = kwargs.pop('params', {})
        params['format'] = 'json'
        if passkey:
            params['passkey'] = self.passkey
        if apikey:
            params['apikey'] = self.apikey
        req = http_get(url, params={} if full_url else params, **kwargs)
        if req.status_code != codes.ok:
            msg = 'cinemate return invalid status code {code} for {url}'
            raise RuntimeError(msg.format(code=req.status_code, url=req.url))
        error = req.json().get('error')
        if error:
            raise RuntimeError(error)
        return req

    def __unicode__(self):
        return '<Cinemate: {username}>'.format(username=self.username)

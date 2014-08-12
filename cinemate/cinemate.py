# coding=utf-8
"""
    Модуль реализует класс Cinemate для хранения пользовательских данных.
"""
from requests import get as http_get
from requests.status_codes import codes
from .utils import BaseCinemate, CinemateConfig, CommonMeta
from .account import Account
from .movie import Movie
from .person import Person
from .stats import Stats


class Cinemate(BaseCinemate):
    """ Класс для хранения пользовательских настроек, таких как
    имя пользователя, пароль, passkey, apikey.

    :param username: имя пользователя
    :type username: :py:class:`str`
    :param password: пароль пользователя
    :type password: :py:class:`str`
    :param passkey: получается
        `в настройках <http://cinemate.cc/preferences/#api>`_
    :type passkey: :py:class:`str`
    :param apikey: получается `через почту <mailto:a@cinemate.cc>`_
    :type apikey: :py:class:`str`
    """
    base_api_url = 'http://api.cinemate.cc/'

    def __init__(self, username='', password='', passkey='', apikey=''):
        """ Инициация главного класса, все остальные создаются внутри.
        """
        if not all((username, password, passkey, apikey)):
            self._config = CinemateConfig()
            self._config.apply(self)
        else:
            self.username = username
            self.password = password
            self.passkey = passkey
            self.apikey = apikey
        self.movie = CommonMeta('Movie', (Movie,), {'cinemate': self})
        self.stats = CommonMeta('Stats', (Stats,), {'cinemate': self})()
        self.person = CommonMeta('Person', (Person,), {'cinemate': self})
        self.account = CommonMeta('Account', (Account,), {'cinemate': self})()

    def api_get(self, url, passkey=False, apikey=False, **kwargs):
        """ Получить страницу API.

        :param url: адрес получаемой страницы, полностью или p/a/th?param=1
        :type url: :py:class:`str`
        :param passkey: использовать для запроса passkey
        :type passkey: :py:class:`bool`
        :param apikey: использовать для запроса apikey
        :type apikey: :py:class:`bool`
        :param kwargs: остальные параметры отправляемые в requests.get
        :type kwargs: :py:class:`dict`
        :return: ответ на запрос
        :raises RuntimeError: вызывается в если в ответе приходит блок error
            или если запрос возвращает некорректный http-статус
        """
        full_url = url.startswith('http://')
        url = full_url and url or self.base_api_url + url.lstrip('/')
        params = kwargs.pop('params', {})
        params['format'] = kwargs.pop('format', 'json')
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

# coding=utf-8
"""
    Модуль реализует класс Stats для получения статистики сайта.
"""
from .utils import BaseCinemate


class Stats(BaseCinemate):
    """ Статистика сайта.
    """
    cinemate = None

    def new(self):
        """ Метод API `stats.new <http://cinemate.cc/help/api/stats.new/>`_
        возвращает статистику сайта за последние сутки.

        :return: словарь содежащий статистику за последние сутки
        :rtype: :py:class:`dict`
        """
        url = 'stats.new'
        req = self.cinemate.api_get(url)
        return req.json()

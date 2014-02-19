# coding=utf-8
"""
    cinemate.stats
    ~~~~~~~~~~~~~~

    Модуль реализует класс Stats для получения статистики сайта.

"""
from .utils import BaseCinemate


class Stats(BaseCinemate):
    """ Статистика сайта
    """
    def new(self):
        """ Метод возвращает статистику сайта за последние сутки
            http://cinemate.cc/help/api/stats.new/
        :return: словарь содежащий статистику за последние сутки
        :rtype: dict
        """
        url = 'stats.new'
        cinemate = getattr(self, 'cinemate')
        req = cinemate.api_get(url)
        return req.json()

# coding=utf-8
from datetime import datetime
from functools import wraps
from six import add_metaclass


class CommonMeta(type):
    pass


@add_metaclass(CommonMeta)
class BaseCinemate(object):
    """ Заглушка для будущего добавления __служебных_методов__
        Для этого же в классах перечислены repr_fields, id_field, full_repr
    """
    pass


def require(attr_name=None):
    """ Декоратор проверяет наличие указаного атрибута у объекта
    :param attr_name: Имя проверяемого атрибута
    :typ attr_name: str
    """
    def outer_wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            instance = getattr(args[0], 'cinemate')
            attr = getattr(instance, attr_name, None)
            if attr is None:
                msg = '{attr} required to use {cls}.{method} method'.format(
                    attr=attr_name,
                    cls=args[0].__class__.__name__,
                    method=func.__name__
                )
                raise ValueError(msg)
            return func(*args, **kwargs)
        return inner_wrapper
    return outer_wrapper


def parse_datetime(source):
    """ Парсинг дат и времени формата (вот четсно: хуй знает какого формата, мне лень
        искать название, но он существует)
        Пример: 2011-04-09T15:38:30
        :param source: Исходная строка с датой
        :type source: str
    """
    if not source:
        return
    return datetime.strptime(source, '%Y-%m-%dT%H:%M:%S')


def parse_date(source):
    """ Парсинг дат формата 2011-04-07
    :param source: Исходная строка с датой
    :type source: str
    """
    if not source:
        return
    return datetime.strptime(source, '%Y-%m-%d')


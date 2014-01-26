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


def require(*attr_names):
    """ Декоратор проверяет наличие указаного атрибута у объекта cinemate
    :param attr_names: проверяемые атрибуты
    :typ attr_names: tuple
    """
    def outer_wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            instance = getattr(args[0], 'cinemate')
            attrs = (getattr(instance, a, None) for a in attr_names)
            if not all(attrs):
                msg = '{attr} required to use {cls}.{method} method'.format(
                    attr=', '.join(attr_names),
                    cls=args[0].__class__.__name__,
                    method=func.__name__
                )
                raise AttributeError(msg)
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


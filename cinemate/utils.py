# coding=utf-8
"""
    cinemate.utils
    ~~~~~~~~~~~~~~

    Модуль реализует
    метакласс CommonMeta для реализации служебных методов;
    класс BaseCinemate от которого наследуются все остальные классы проекта;
    декоратор require, который проверяет у экземпляра класса наличие
        указаных аттрибутов;
    функции parse_date, parse_datetime для разбора дат и времени в формате ISO.

"""
from datetime import datetime
from functools import wraps
from six import add_metaclass, PY2, callable


class CommonMeta(type):
    """ Метакласс для реализации служебных методов
    """
    pass

@add_metaclass(CommonMeta)
class BaseCinemate(object):
    """ Заглушка для будущего добавления __служебных_методов__
        Для этого же в классах перечислены repr_fields, id_field, full_repr
    """
    def __str__(self):
        unicode_method = getattr(self, '__unicode__')
        if callable(unicode_method):
            unicode_method = unicode_method()
        return PY2 and unicode_method.encode('utf-8') or unicode_method


def require(*attr_names):
    """ Декоратор проверяет наличие указаного атрибута у объекта cinemate
    :param attr_names: проверяемые атрибуты
    :type attr_names: tuple
    :return: Оборачиваемый метод
    """
    def outer_wrapper(method):
        """ Обёртка для метода
        :param method: Оборачиваемый метод
        """
        @wraps(method)
        def inner_wrapper(*args, **kwargs):
            """ Обёртка для функции
            :param args: неименованные параметры декорируемой функции
            :param kwargs: именованные параметры декорируемой функции
            :raises AttributeError: Вызывается, если объект не содержит
                требуемых полей
            """
            instance = getattr(args[0], 'cinemate')
            if not all(hasattr(instance, a) for a in attr_names):
                msg = '{attr} required to use {cls}.{method} method'.format(
                    attr=', '.join(attr_names),
                    cls=args[0].__class__.__name__,
                    method=method.__name__
                )
                raise AttributeError(msg)
            return method(*args, **kwargs)
        return inner_wrapper
    return outer_wrapper


def parse_datetime(source):
    """ Парсинг дат и времени формата ISO. Например: 2011-04-09T15:38:30
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


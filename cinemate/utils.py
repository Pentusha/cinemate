# coding=utf-8
"""
    Модуль содержит:
    метакласс :class:`.CommonMeta` для реализации служебных методов;
    - класс :class:`.BaseCinemate` от которого наследуются все остальные
      классы проекта;
    - декоратор :func:`require`, который проверяет у экземпляра класса наличие
      указаных аттрибутов;
    - функции :func:`parse_date`, :func:`parse_datetime` для разбора дат и
      времени в формате ISO.

"""
from datetime import datetime
from functools import wraps
from six import add_metaclass, PY2


class CommonMeta(type):
    """ Метакласс для реализации __служебных_методов__.
    """
    def __new__(mcs, name, bases, attrs):
        method = attrs.get('__unicode__')
        if method:
            to_str = lambda x: PY2 and method(x).encode('utf-8') or method(x)
            attrs.setdefault('__str__', to_str)
            attrs.setdefault('__repr__', to_str)
        return super(CommonMeta, mcs).__new__(mcs, name, bases, attrs)


@add_metaclass(CommonMeta)
class BaseCinemate(object):
    """ От этого класса наследуются все остальные классы проекта.
    """


# noinspection PyPep8Naming
class require(object):
    """ Декоратор проверяет наличие указанных атрибутов у объекта cinemate.
    """
    def __init__(self, *attr_names):
        """
        :param attr_names: имена требуемых аттрибутов
        :type attr_names: :py:class:`str` or :py:class:`tuple`
        """
        self.attr_names = attr_names

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """ Декорируемая функция.

            :param args: неименованные параметры декорируемой функции
            :type args: :py:class:`tuple`
            :param kwargs: именованные параметры декорируемой функции
            :type kwargs: :py:class:`dict`
            """
            cinemate = __get_cinemate__(args[0])  # args[0] == self or cls
            if not all(getattr(cinemate, a, None) for a in self.attr_names):
                msg = '{attr} required to use {cls}.{method} method'.format(
                    attr=', '.join(self.attr_names),
                    cls=args[0].__class__.__name__,
                    method=func.__name__
                )
                raise AttributeError(msg)
            return func(*args, **kwargs)
        return wrapper


def __get_cinemate__(instance):
    """ Получение объекта cinemate хранящегося в аттрибутах.

    :param instance: экземпляр какого-нибудь класса
    :return: объект cinemate
    :raises AttributeError: Вызывается, если объект не содержит
        требуемых полей или экземпляра cinemate
    """
    if hasattr(instance, 'cinemate'):
        return getattr(instance, 'cinemate')
    elif instance.__class__.__name__ == 'Cinemate':  # avoid cycle imports
        return instance
    else:
        raise AttributeError('Object has not cinemate attribute')


def parse_datetime(source):
    """ Парсинг дат и времени формата ISO. Например: 2011-04-09T15:38:30

    :param source: исходная строка с датой и временем
    :type source: :py:class:`str`
    """
    if not source:
        return
    return datetime.strptime(source, '%Y-%m-%dT%H:%M:%S')


def parse_date(source):
    """ Парсинг дат формата 2011-04-07

    :param source: исходная строка с датой
    :type source: :py:class:`str`
    """
    if not source:
        return
    return datetime.strptime(source, '%Y-%m-%d')

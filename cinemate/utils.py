# coding=utf-8
"""
    Модуль содержит:
    - класс :class:`.CinemateConfig` для работы с настройками;
    - метакласс :class:`.CommonMeta` для реализации служебных методов;
    - класс :class:`.BaseCinemate` от которого наследуются все остальные
      классы проекта;
    - классы :class:`.BaseImage` и :class:`.BaseSlug` в которые вынесен общий
      код для :class:`person.Photo`, :class:`movie.Poster`,
      :class:`movie.Country`, :class:`movie.Genre`;
    - декоратор :func:`require`, который проверяет у экземпляра класса наличие
      указаных аттрибутов;
    - функции :func:`parse_date`, :func:`parse_datetime` для разбора дат и
      времени в формате ISO.

"""
import yaml
import __main__ as main
from datetime import datetime
from functools import wraps
from getpass import getpass
from os.path import exists, expanduser, join
from six import add_metaclass, iteritems, PY2
from six.moves import input


def _open(*args, **kwargs):  # pragma: no cover
    """ Используется для подмены содержимого при тестировании
    """
    return open(*args, **kwargs)


def _exists(*args, **kwargs):  # pragma: no cover
    return exists(*args, **kwargs)


class CinemateConfig(object):
    """ Класс для чтения и сохранения конфигурации.
    """
    module = yaml
    filename = join(expanduser('~'), '.cinemate')
    _auth = {}.fromkeys(('username', 'password', 'apikey', 'passkey'))
    _config = {'auth': _auth}

    def __init__(self):
        interactive = not hasattr(main, '__file__')
        if interactive and not self.exists:  # pragma: no cover
            self.interactive_input()
            self.save()
        elif not self.exists:
            msg = (
                'Config file {cfg} does not exists. Create it manually '
                'or create cinemate instance in interactive mode:\n'
                '>>> from cinemate import Cinemate\n'
                '>>> cin = Cinemate()'
            )
            raise IOError(msg.format(cfg=self.filename))
        else:
            self.load()

    @property
    def exists(self, filename=None):
        return _exists(filename or self.filename)

    def interactive_input(self):  # pragma: no cover
        """ Запрашивает у пользователя данные и сохраняет их.
        """
        self._auth['username'] = input('Username: ')
        self._auth['password'] = getpass('Password: ')
        self._auth['passkey'] = getpass('Passkey: ')
        self._auth['apikey'] = getpass('Apikey: ')

    def apply(self, obj):
        """ Сохраняет пользовательские настройки в указанный объект.
        """
        for field, value in iteritems(self._auth):
            setattr(obj, field, value)

    def load(self, filename=None):
        """ Загружает пользовательские данные из файла.
        :param filename: имя файла, если не задано используется значение
            по умолчанию: ``~/.cinemate`` или ``%HOME%\.cinemate``
            в зависимости от операционной системы
        :type filename: :py:class:`str`
        """
        with _open(filename or self.filename) as cfg:
            self._config = self.module.load(cfg)
            self._auth = self._config['auth']

    def save(self, filename=None):
        """ Сохраняет пользовательские настройки в файл.
        :param filename: имя файла
        :type filename: :py:class:`str`
        """
        for field, value in iteritems(self._auth):
            self._config['auth'][field] = value
        with _open(filename or self.filename, 'w') as cfg:
            self.module.dump(self._config, cfg, default_flow_style=False)


class CompareMixin(object):
    id = None

    def __eq__(self, other):
        return type(self) is type(other) and self.id == other.id


class FieldsCompareMixin(object):
    fields = []

    def __eq__(self, other):
        is_dict = isinstance(self.fields, dict)
        fields = self.fields.keys() if is_dict else self.fields
        return all(getattr(self, f) == getattr(other, f) for f in fields)


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


class BaseImage(FieldsCompareMixin, BaseCinemate):
    fields = ('small', 'medium', 'big')

    def __init__(self, small, medium, big):
        self.small = small
        self.medium = medium
        self.big = big

    @classmethod
    def from_dict(cls, dct):
        """ Изображение из словаря, возвращаемого API.

        :param dct: словарь, возвращаемый API
        :type dct: :py:class:`dict`
        :return: изображение
        :rtype: :class:`{module_name}.{class_name}`
        """.format(
            module_name=cls.__module__,
            class_name=cls.__name__,
        )
        if dct is None:
            return
        fields = {k: dct.get(k).get('url') for k in cls.fields if k in dct}
        return cls(**fields)

    def __unicode__(self):
        sizes = '/'.join(k for k, v in sorted(iteritems(self.__dict__)) if v)
        return '<{class_name} {sizes}>'.format(
            class_name=self.__class__.__name__,
            sizes=sizes,
        )


class BaseSlug(BaseCinemate):
    def __init__(self, name, slug=None):
        self.name = name
        self.slug = slug or self.slug_by_name(name)

    @classmethod
    def from_dict(cls, dct):
        """ Задать объект из словаря, возвращаемого API.

        :param dct: словарь, возвращаемый API
        :type dct: :py:class:`dict`
        :return: объект
        :rtype: :class:`{module_name}.{class_name}`
        """.format(
            module_name=cls.__module__,
            class_name=cls.__name__,
        )
        name = dct.get('name')
        slug = dct.get('slug', cls.slug_by_name(name))
        return cls(name=name, slug=slug)

    @classmethod
    def slug_by_name(cls, name):
        """ Получение slug объекта по его названию на русском языке.

        :param name: имя объекта на русском языке
        :return: slug объекта
        :rtype: :py:class:`str`
        """
        finder = (slug for slug, rus in iteritems(cls.mapping) if rus == name)
        return next(finder, None)

    def __eq__(self, other):
        return self.slug == other.slug or self.name == other.name

    def __unicode__(self):
        return '<{class_name}: {name}>'.format(
            class_name=self.__class__.__name__,
            name=self.slug or self.name,
        )


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

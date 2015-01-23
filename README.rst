|version| |docs| |build| |coverage| |wheel|

Cinemate - реализация API сайта `cinemate.cc`_ на языке python.
Реализация использует методы `api v2`_.

Установка
=========
Используйте следующую команду для получения последней версии::

    pip install cinemate

Страница на PyPI_.

Документация на `Read the Docs`_.

Использование
=============
Ниже приведены простые примеры, подробные примеры находятся в каталоге examples_.

Инициализация:

.. code:: python

    >>> from cinemate import Cinemate
    >>> cin = Cinemate('username', 'password', 'passkey', 'apikey')

Получить подробную информацию о персоне:

.. code:: python

    >>> person = cin.person.get(57658)
    >>> print(person)
    <Person 57658 Noel Fielding>
    >>> print(person.photo.big)
    http://c.cinemate.cc/media/p/8/5/57658/0.big.jpg

Получить подробную информацию о фильме:

.. code:: python

    >>> print(movie)
    <Movie 114458 Africa>
    >>> print(movie.title.original)
    Africa
    >>> movie.runtime is None
    True
    >>> print(movie.imdb)
    <Rating rating=8.9 votes=1984>
    >>> print(movie.imdb.rating)
    8.9

Получить список слежения пользователя:

.. code:: python

    >>> watchlist = cin.account.watchlist()
    >>> for person in watchlist['person']:
    ...     print(person.name_original)
    ...
    Kar Wai Wong
    Gregg Araki
    Jan Svankmajer
    Gaspar Noe

Участие в разработке
====================
Проверяйте внесенные изменения на соответсвие pep-20_, pep-8_, pep-287_.
Пожалуйста, документируйте код на русском языке, т.к. проект cinemate.cc рассчитан на русскоговорящую аудиторию.

Тесты запускаются через tox_ и должны выполняться в версиях py27, py32, py33, py34, pypy, pypy3.

В остальном никаких особенностей нет, форкаете, меняете, pull-request.


.. _cinemate.cc: http://cinemate.cc/
.. _api v2: http://cinemate.cc/help/api/
.. _examples: https://github.com/Pentusha/cinemate/tree/master/examples
.. _PyPI: https://pypi.python.org/pypi/cinemate
.. _Read the Docs: http://cinemate.rtfd.org/
.. _pep-20: http://www.python.org/dev/peps/pep-0020/
.. _pep-8: http://www.python.org/dev/peps/pep-0008/
.. _pep-287: http://www.python.org/dev/peps/pep-0287/
.. _tox: https://pypi.python.org/pypi/tox

.. |version| image:: http://badge.fury.io/py/cinemate.svg
   :alt: PyPI version
   :target: http://badge.fury.io/py/cinemate
.. |docs| image:: https://readthedocs.org/projects/cinemate/badge/?version=latest
   :alt: Docs status
   :target: https://readthedocs.org/builds/cinemate/
.. |build| image:: http://secure.travis-ci.org/Pentusha/cinemate.png?branch=master
   :alt: Build status
   :target: https://travis-ci.org/Pentusha/cinemate
.. |coverage| image:: http://coveralls.io/repos/Pentusha/cinemate/badge.svg?branch=master
   :alt: Tests Coverage
   :target: https://coveralls.io/r/Pentusha/cinemate
.. |wheel| image:: http://pypip.in/wheel/cinemate/badge.svg?style=flat
   :alt: Wheel Status
   :target: https://pypi.python.org/pypi/cinemate/

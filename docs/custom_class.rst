Расширение функционала
======================

Можно расширить базовый функционал библиотеки собственными методами и классами.

Пример:

.. code-block:: python

    from requests import session
    from cinemate import Cinemate, Movie
    from cinemate.utils import BaseCinemate


    class MovieWithLinks(Movie):
        """ Добавление дополнительного метода к основному классу. """
        def links(self):
            return self.cinemate.link.for_movie(self.id)


    class Link(BaseCinemate):
        """ Собственный класс для работы с ссылками. """
        @classmethod
        def for_movie(cls, movie_id):
            # your code here


    class CinemateExtra(Cinemate):
        """ Переопределение главного класса. """
        def __init__(self, *args, **kwargs):
            super(CinemateExtra, self).__init__(*args, **kwargs)
            self.session = session()
            self.movie = type('movie', (MovieWithLinks,), {'cinemate': self})
            self.link = type('link', (Link,), {'cinemate': self})

        def login(self):
            # your code here

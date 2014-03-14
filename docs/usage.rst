Использование
=============

Для начала использования библиотеки необходимо инициализировать основной класс:

.. code-block:: python

    from cinemate import Cinemate

    cin = Cinemate(
        'your_username',
        'your_password',
        'your_passkey',
        'your_apikey'
    )

Доступ к методам api осуществляется через аттрибуты объекта cinemate.
Ниже приведена таблица сооветсвия методов API и данной реализации.

=======================================================================  ============================================================  ==============================================================
Метод API                                                                Описание                                                      Метод реализации
=======================================================================  ============================================================  ==============================================================
`account.auth <http://cinemate.cc/help/api/account.auth/>`_              Авторизация по логину и паролю                                :meth:`cin.account.auth() <cinemate.Account.auth>`
`account.profile <http://cinemate.cc/help/api/account.profile/>`_        Данные и статистика пользовательского аккаунта                :meth:`cin.account.profile() <cinemate.Account.profile>`
`account.updatelist <http://cinemate.cc/help/api/account.updatelist/>`_  Записи ленты обновлений пользователя                          :meth:`cin.account.updatelist() <cinemate.Account.updatelist>`
`account.watchlist <http://cinemate.cc/help/api/account.watchlist/>`_    Метод возвращает список объектов слежения пользователя        :meth:`cin.account.watchlist() <cinemate.Account.watchlist>`
`movie <http://cinemate.cc/help/api/movie/>`_                            Информация о фильме                                           :meth:`cin.movie.get(id) <cinemate.Movie.get>`
`movie.list <http://cinemate.cc/help/api/movie.list/>`_                  Результаты поиска фильмов, используя заданные фильтры         :meth:`cin.movie.list() <cinemate.Movie.list>`
`movie.search <http://cinemate.cc/help/api/movie.search/>`_              Поиск по заголовкам фильмов                                   :meth:`cin.movie.search() <cinemate.Movie.search>`
`person <http://cinemate.cc/help/api/person/>`_                          Основная информация о персоне                                 :meth:`cin.person.get(id) <cinemate.Person.get>`
`person.movies <http://cinemate.cc/help/api/person.movies/>`_            Фильмы, в съемке которых персона принимала участие            :meth:`cin.person(id).movies() <cinemate.Person.movies>`
`person.search <http://cinemate.cc/help/api/person.search/>`_            Метод возвращает первые 10 результатов поиска по базе персон  :meth:`cin.person.search() <cinemate.Person.search>`
`stats.new <http://cinemate.cc/help/api/stats.new/>`_                    Метод возвращает статистику сайта за последние сутки          :meth:`cin.stats.new() <cinemate.Stats.new>`
=======================================================================  ============================================================  ==============================================================

Примеры использования некоторых методов приведены в `репозитарии <https://github.com/Pentusha/cinemate/tree/master/examples>`_.

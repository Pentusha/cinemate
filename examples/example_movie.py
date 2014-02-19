# coding=utf-8
""" Пример показывает как использовать следующие методы api:
    * movie
    * movie.list
    * movie.search
"""
from six import u
from cinemate import Cinemate


if __name__ == '__main__':
    cin = Cinemate(
        'username',
        'password',
        'passkey',
        'apikey'
    )
    africa = cin.movie.get(114458)
    print(africa.poster.big)
    for person in africa.cast:
        print(person)
    print(africa.description)

    found = cin.movie.search(u('в поисках'))
    for mov in found:
        print(mov)

    documentary = africa.genre[0]
    print(documentary)

    lst = cin.movie.list(year=2010, genre=documentary, per_page=25)
    # аналогично cin.movie.list(year=2010, genre='documentary', per_page=25)
    # жанры и страны хранятся в cinemate.genres и cinemate.countries
    for mov in lst:
        print(mov)

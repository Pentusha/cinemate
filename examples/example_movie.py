# coding=utf-8
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

    lst = cin.movie.list(year=2010, country='russia', per_page=25)
    for mov in lst:
        print(mov)

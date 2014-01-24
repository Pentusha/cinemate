# coding=utf-8
from cinemate import Cinemate

if __name__ == '__main__':
    cin = Cinemate(
        'username',
        'password',
        'passkey',
        'apikey'
    )
    noel = cin.person.get(57658)
    print(noel)
    print(noel.photo.big)
    movies = noel.movies()
    for mov in movies['actor']:
        print(mov)

    found = cin.person.search(u'акира')
    for person in found:
        print(person)



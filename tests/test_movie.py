# coding=utf-8
from datetime import date, datetime

import pytest
from pytest_httpretty import stub_get
from six import u

from cinemate.movie import Title, Poster, Release, Rating, Country, Genre


def test_poster():
    poster = 'http://c.cinemate.cc/media/images/poster/2010/68675/1298810716'
    poster = Poster(
        small=poster + '.small.jpg',
        medium=poster + '.medium.jpg',
        big=poster + '.big.jpg'
    )
    assert str(poster) == '<Poster big/medium/small>'


def test_title():
    title = Title(u('Криминальная фишка от Генри'), 'Henry\'s Crime')
    assert str(title) == 'Henry\'s Crime'


def test_release():
    release = Release(world='2011-04-07', russia='2011-04-07')
    assert str(release) == '<Release russia/world>'


def test_rating():
    imdb = Rating(rating=5.9, votes=12147)
    assert str(imdb) == '<Rating rating=5.9 votes=12147>'
    kp = Rating(rating=5.0, votes=12000)
    assert imdb != kp


def test_country():
    country = Country(name=u('США'))
    assert str(country) == '<Country: usa>'


@pytest.mark.httpretty
def test_movie(cin, rr):
    stub_get(**rr['movie'])
    mov = cin.movie.get(68675)
    assert str(mov) == '<Movie 68675 Henry\'s Crime>'

    assert mov.country == [Country(name=u('США'))]
    assert mov.genre == [Genre(name=u('комедия'))]

    assert mov.director == [
        cin.person(163239, name=u('Малькольм Венвилль'))
    ]

    actors = (
        2624, 1219, 2856, 112, 2243, 9803, 13257, 39646,
        9040, 5933, 67860, 108757, 190286, 148348, 190285,
    )
    assert mov.cast == list(map(cin.person, actors))

    assert mov.url == 'http://cinemate.cc/movie/68675/'

    stub_get(**rr['movie_one_person'])
    mov = cin.movie.get(147668)
    assert isinstance(mov.cast, list)


@pytest.mark.httpretty
def test_movie_list(cin, rr):
    stub_get(**rr['movie.list'])
    movies = (
        131001, 131657, 109767, 83460, 66450,
        135826, 105524, 122874, 133159, 52036,
    )
    assert cin.movie.list() == list(map(cin.movie, movies))

    stub_get(**rr['movie.list_with_params'])
    lst = cin.movie.list(
        order_from=date(1988, 7, 4),
        order_to=datetime(1989, 7, 4),
        order_by='release_date'
    )
    movies = (
        24424, 6685, 114718, 32660, 117681,
        38105, 18319, 7139, 14832, 19272,
    )
    assert lst == list(map(cin.movie, movies))

    with pytest.raises(ValueError):
        cin.movie.list(
            order_from=date(1988, 7, 4),
            order_to=datetime(1989, 7, 4)
        )


@pytest.mark.httpretty
def test_movie_search(cin, rr):
    stub_get(**rr['movie.search'])
    lst = cin.movie.search(u('Пираты кариб'))
    movies = 120787, 68669, 1787, 2194, 15869, 7412
    assert lst == list(map(cin.movie, movies))

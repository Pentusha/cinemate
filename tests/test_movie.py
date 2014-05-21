# coding=utf-8
from datetime import date, datetime

import pytest
from pytest_httpretty import stub_get
from six import u


from cinemate.movie import Title, Poster, Release, Rating, Country, Genre
from tests.mock import reqresp as rr


@pytest.mark.httpretty
def test_movie(cin):
    stub_get(**rr['movie'])
    mov = cin.movie.get(68675)
    assert str(mov) == '<Movie 68675 Henry\'s Crime>'
    assert mov.id == 68675
    assert mov.type == 'movie'
    test_title = Title(u('Криминальная фишка от Генри'), 'Henry\'s Crime')
    assert mov.title.english == test_title.english
    assert str(mov.title) == 'Henry\'s Crime'
    assert mov.title.russian == test_title.russian
    assert mov.title.original == test_title.original
    assert mov.year == 2010
    poster = 'http://c.cinemate.cc/media/images/poster/2010/68675/1298810716'
    test_poster = Poster(
        small=poster + '.small.jpg',
        medium=poster + '.medium.jpg',
        big=poster + '.big.jpg'
    )
    assert str(mov.poster) == '<Poster big/medium/small>'
    assert mov.poster.small == test_poster.small
    assert mov.poster.medium == test_poster.medium
    assert mov.poster.big == test_poster.big
    description = u(
        'Встречайте Генри – самого унылого парня в Америке. Он сидит в своей б'
        'удке у дороги, взимая пошлину с проезжающих. Казалось, в его жизни ни'
        'что не может измениться. Но однажды сомнительный приятель попросил Ге'
        'нри подождать его у крыльца главного банка в Буффало... В результате '
        '– четыре года тюрьмы по ложному обвинению в ограблении. Но пройдет вр'
        'емя, и Генри вернется к тому самому банку, чтобы взять свое…'
    )
    assert mov.description == description
    assert mov.runtime == 108
    test_release = Release(world='2011-04-07', russia='2011-04-07')
    assert str(mov.release) == '<Release russia/world>'
    assert mov.release.world == test_release.world
    assert mov.release.russia == test_release.russia
    test_imdb = Rating(rating=5.9, votes=12147)
    assert str(mov.imdb) == '<Rating rating=5.9 votes=12147>'
    assert mov.imdb.rating == test_imdb.rating
    assert mov.imdb.votes == test_imdb.votes
    test_kp = Rating(rating=6.2, votes=11673)
    assert mov.kinopoisk.rating == test_kp.rating
    assert mov.kinopoisk.votes == test_kp.votes
    test_country = Country(name=u('США'))
    assert isinstance(mov.country, list)
    assert len(mov.country) == 1
    assert isinstance(mov.country[0], Country)
    assert str(mov.country[0]) == u('<Country: usa>')
    assert mov.country[0].name == test_country.name
    test_genre = Genre(name=u('комедия'))
    assert isinstance(mov.genre, list)
    assert len(mov.genre) == 1
    assert isinstance(mov.genre[0], Genre)
    assert str(mov.genre[0]) == u('<Genre: comedy>')
    assert mov.genre[0].name == test_genre.name

    test_director = cin.person(163239, name=u('Малькольм Венвилль'))
    assert isinstance(mov.director, list)
    assert len(mov.director) == 1
    # assert str(mov.director[0]) == u('<Person 163239 Малькольм Венвилль>')
    assert isinstance(mov.director[0], cin.person)
    assert mov.director[0].name == test_director.name

    test_actor = cin.person(2624, name=u('Киану Ривз'))
    assert isinstance(mov.cast, list)
    assert len(mov.cast) == 15
    # assert str(mov.cast[0]) == u('<Person 2624 Киану Ривз>')
    assert isinstance(mov.cast[0], cin.person)
    assert mov.cast[0].name == test_actor.name
    assert mov.url == 'http://cinemate.cc/movie/68675/'

    stub_get(**rr['movie_one_person'])
    mov = cin.movie.get(147668)
    assert isinstance(mov.cast, list)


@pytest.mark.httpretty
def test_movie_list(cin):
    stub_get(**rr['movie.list'])
    lst = cin.movie.list()
    assert isinstance(lst, list)
    assert len(lst) == 10
    assert isinstance(lst[0], cin.movie)
    assert lst[0].id == 131001

    stub_get(**rr['movie.list_with_params'])
    lst = cin.movie.list(
        order_from=date(1988, 7, 4),
        order_to=datetime(1989, 7, 4),
        order_by='release_date'
    )
    assert isinstance(lst, list)
    assert len(lst) == 10
    assert isinstance(lst[0], cin.movie)
    assert lst[0].id == 24424
    with pytest.raises(ValueError):
        cin.movie.list(
            order_from=date(1988, 7, 4),
            order_to=datetime(1989, 7, 4)
        )


@pytest.mark.httpretty
def test_movie_search(cin):
    stub_get(**rr['movie.search'])
    lst = cin.movie.search(u('Пираты кариб'))
    assert isinstance(lst, list)
    assert len(lst) == 6
    assert isinstance(lst[0], cin.movie)
    assert lst[0].id == 120787

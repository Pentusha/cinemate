# coding=utf-8
import pytest
from pytest_httpretty import stub_get
from six import u

from cinemate.person import Photo
from tests.mock import reqresp as rr


@pytest.mark.httpretty
def test_person(cin):
    stub_get(**rr['person'])
    person = cin.person.get(3971)
    assert isinstance(person, cin.person)
    assert person.name == u('Джейк Джилленхол')
    assert person.name_original == 'Jake Gyllenhaal'
    photo = 'http://c.cinemate.cc/media/images/photo/j/3971/1290595484'
    test_photo = Photo(
        small=photo + '.small.jpg',
        medium=photo + '.medium.jpg',
        big=photo + '.big.jpg'
    )
    assert isinstance(person.photo, Photo)
    assert str(person.photo) == '<Photo big/medium/small>'
    assert person.photo.small == test_photo.small
    assert person.photo.medium == test_photo.medium
    assert person.photo.big == test_photo.big
    assert person.url == 'http://cinemate.cc/person/3971/'
    assert str(person) == '<Person 3971 Jake Gyllenhaal>'


@pytest.mark.httpretty
def test_person_movies(cin):
    stub_get(**rr['person.movies'])
    movies = cin.person(43083).movies()
    assert isinstance(movies, dict)

    assert 'director' in movies
    director_movies = movies['director']
    assert isinstance(director_movies, list)
    assert len(director_movies) == 5
    movie = director_movies[0]
    assert isinstance(movie, cin.movie)
    assert movie.id == 79144
    assert movie.type == 'movie'
    assert movie.runtime == 105

    assert 'actor' in movies
    actor_movies = movies['actor']
    assert isinstance(actor_movies, list)
    assert len(actor_movies) == 2
    movie = actor_movies[0]
    assert isinstance(movie, cin.movie)
    assert movie.id == 79144
    assert movie.type == 'movie'
    assert movie.runtime == 105


@pytest.mark.httpretty
def test_person_search(cin):
    stub_get(**rr['person.search'])
    lst = cin.person.search(u('гиленхол'))
    assert isinstance(lst, list)
    assert len(lst) == 7
    person = lst[0]
    assert isinstance(person, cin.person)
    assert person.id == 3971
    assert person.name == u('Джейк Джилленхол')
    assert person.name_original == 'Jake Gyllenhaal'
    photo = 'http://c.cinemate.cc/media/images/photo/j/3971/1290595484'
    test_photo = Photo(
        small=photo + '.small.jpg',
        medium=photo + '.medium.jpg',
        big=photo + '.big.jpg'
    )
    assert isinstance(person.photo, Photo)
    assert person.photo.small == test_photo.small
    assert person.photo.medium == test_photo.medium
    assert person.photo.big == test_photo.big
    assert person.url == 'http://cinemate.cc/person/3971/'

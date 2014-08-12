# coding=utf-8
import pytest
from pytest_httpretty import stub_get
from six import u


@pytest.mark.httpretty
def test_person(cin, rr):
    stub_get(**rr['person'])
    person = cin.person.get(3971)
    assert str(person) == '<Person 3971 Jake Gyllenhaal>'


@pytest.mark.httpretty
def test_person_movies(cin, rr):
    stub_get(**rr['person.movies'])
    movies = cin.person(43083).movies()
    assert isinstance(movies, dict)

    director_movies = movies['director']
    lst = 79144, 4974, 31965, 4703, 5509
    assert director_movies == list(map(cin.movie, lst))

    actor_movies = movies['actor']
    lst = 79144, 4974
    assert actor_movies == list(map(cin.movie, lst))


@pytest.mark.httpretty
def test_person_search(cin, rr):
    stub_get(**rr['person.search'])
    lst = cin.person.search(u('гиленхол'))
    persons = 3971, 1685, 79826, 76362, 361603, 303647, 333519
    assert lst == list(map(cin.person, persons))

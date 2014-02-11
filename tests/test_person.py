# coding=utf-8
from httpretty import activate, register_uri, GET
from tests.test_cinemate import CinemateTestCase
from tests.mock import reqresp as rr
from six import u
from cinemate.person import Photo


class PersonTestCase(CinemateTestCase):
    @activate
    def test_person(self):
        register_uri(GET,
                     rr['person']['req'],
                     body=rr['person']['resp'])
        person = self.cin.person.get(3971)
        self.assertIsInstance(person, self.cin.person)
        self.assertEqual(person.name, u('Джейк Джилленхол'))
        self.assertEqual(person.name_original, 'Jake Gyllenhaal')
        test_photo = Photo(
            small='http://c.cinemate.cc/media/images/photo/j/3971/1290595484.small.jpg',
            medium='http://c.cinemate.cc/media/images/photo/j/3971/1290595484.medium.jpg',
            big='http://c.cinemate.cc/media/images/photo/j/3971/1290595484.big.jpg'
        )
        self.assertIsInstance(person.photo, Photo)
        self.assertEqual(str(person.photo), '<Photo big/medium/small>')
        self.assertEqual(person.photo.small, test_photo.small)
        self.assertEqual(person.photo.medium, test_photo.medium)
        self.assertEqual(person.photo.big, test_photo.big)
        self.assertEqual(person.url, 'http://cinemate.cc/person/3971/')
        self.assertEqual(str(person), '<Person 3971 Jake Gyllenhaal>')

    @activate
    def test_person_movies(self):
        register_uri(GET,
                     rr['person.movies']['req'],
                     body=rr['person.movies']['resp'])
        movies = self.cin.person(43083).movies()
        self.assertIsInstance(movies, dict)

        self.assertIn('director', movies)
        director_movies = movies['director']
        self.assertIsInstance(director_movies, list)
        self.assertEqual(len(director_movies), 5)
        movie = director_movies[0]
        self.assertIsInstance(movie, self.cin.movie)
        self.assertEqual(movie.id, 79144)
        self.assertEqual(movie.type, 'movie')
        self.assertEqual(movie.runtime, 105)

        self.assertIn('actor', movies)
        actor_movies = movies['actor']
        self.assertIsInstance(actor_movies, list)
        self.assertEqual(len(actor_movies), 2)
        movie = actor_movies[0]
        self.assertIsInstance(movie, self.cin.movie)
        self.assertEqual(movie.id, 79144)
        self.assertEqual(movie.type, 'movie')
        self.assertEqual(movie.runtime, 105)

    @activate
    def test_person_search(self):
        register_uri(GET,
                     rr['person.search']['req'],
                     body=rr['person.search']['resp'])
        lst = self.cin.person.search(u('гиленхол'))
        self.assertIsInstance(lst, list)
        self.assertEqual(len(lst), 7)
        person = lst[0]
        self.assertIsInstance(person, self.cin.person)
        self.assertEqual(person.id, 3971)
        self.assertEqual(person.name, u('Джейк Джилленхол'))
        self.assertEqual(person.name_original, 'Jake Gyllenhaal')
        test_photo = Photo(
            small='http://c.cinemate.cc/media/images/photo/j/3971/1290595484.small.jpg',
            medium='http://c.cinemate.cc/media/images/photo/j/3971/1290595484.medium.jpg',
            big='http://c.cinemate.cc/media/images/photo/j/3971/1290595484.big.jpg'
        )
        self.assertIsInstance(person.photo, Photo)
        self.assertEqual(person.photo.small, test_photo.small)
        self.assertEqual(person.photo.medium, test_photo.medium)
        self.assertEqual(person.photo.big, test_photo.big)
        self.assertEqual(person.url, 'http://cinemate.cc/person/3971/')

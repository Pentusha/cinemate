# coding=utf-8
from cinemate.movie import Title, Poster, Release, Rating, Country, Genre
from httpretty import activate, register_uri, GET
from tests.test_cinemate import CinemateTestCase
from tests.mock import reqresp as rr


class MovieTestCase(CinemateTestCase):
    @activate
    def test_movie(self):
        register_uri(GET,
                     rr['movie']['req'],
                     body=rr['movie']['resp'])
        mov = self.cin.movie(68675).fetch()
        self.assertEqual(mov.id, 68675)
        self.assertEqual(mov.type, 'movie')
        test_title = Title(u'Криминальная фишка от Генри', 'Henry\'s Crime')
        self.assertEqual(mov.title.english, test_title.english)
        self.assertEqual(mov.title.russian, test_title.russian)
        self.assertEqual(mov.title.original, test_title.original)
        self.assertEqual(mov.year, 2010)
        test_poster = Poster(
            small='http://c.cinemate.cc/media/images/poster/2010/68675/1298810716.small.jpg',
            medium='http://c.cinemate.cc/media/images/poster/2010/68675/1298810716.medium.jpg',
            big='http://c.cinemate.cc/media/images/poster/2010/68675/1298810716.big.jpg'
        )
        self.assertEqual(mov.poster.small, test_poster.small)
        self.assertEqual(mov.poster.medium, test_poster.medium)
        self.assertEqual(mov.poster.big, test_poster.big)
        self.maxDiff = 1000
        self.assertEqual(mov.description, u'Встречайте Генри – самого унылого парня в Америке. Он сидит в своей будке у дороги, взимая пошлину с проезжающих. Казалось, в его жизни ничто не может измениться. Но однажды сомнительный приятель попросил Генри подождать его у крыльца главного банка в Буффало... В результате – четыре года тюрьмы по ложному обвинению в ограблении. Но пройдет время, и Генри вернется к тому самому банку, чтобы взять свое…')
        self.maxDiff = 640
        self.assertEqual(mov.runtime, 108)
        test_release = Release(world='2011-04-07', russia='2011-04-07')
        self.assertEqual(mov.release.world, test_release.world)
        self.assertEqual(mov.release.russia, test_release.russia)
        test_imdb = Rating(rating='5.9', votes='12147')
        self.assertEqual(mov.imdb.rating, test_imdb.rating)
        self.assertEqual(mov.imdb.votes, test_imdb.votes)
        test_kp = Rating(rating='6.2', votes='11673')
        self.assertEqual(mov.kinopoisk.rating, test_kp.rating)
        self.assertEqual(mov.kinopoisk.votes, test_kp.votes)
        test_country = Country(name=u'США')
        self.assertIsInstance(mov.country, list)
        self.assertEqual(len(mov.country), 1)
        self.assertIsInstance(mov.country[0], Country)
        self.assertEqual(mov.country[0].name, test_country.name)
        test_genre = Genre(name=u'комедия')
        self.assertIsInstance(mov.genre, list)
        self.assertEqual(len(mov.genre), 1)
        self.assertIsInstance(mov.genre[0], Genre)
        self.assertEqual(mov.genre[0].name, test_genre.name)
        test_director = self.cin.person(163239, name=u'Малькольм Венвилль')
        self.assertIsInstance(mov.director, list)
        self.assertEqual(len(mov.director), 1)
        self.assertIsInstance(mov.director[0], self.cin.person)
        self.assertEqual(mov.director[0].name, test_director.name)
        test_actor = self.cin.person(2624, name=u'Киану Ривз')
        self.assertIsInstance(mov.cast, list)
        self.assertEqual(len(mov.cast), 15)
        self.assertIsInstance(mov.cast[0], self.cin.person)
        self.assertEqual(mov.cast[0].name, test_actor.name)
        self.assertEqual(mov.url, 'http://cinemate.cc/movie/68675/')

    @activate
    def test_movie_list(self):
        register_uri(GET,
                     rr['movie.list']['req'],
                     body=rr['movie.list']['resp'])
        lst = self.cin.movie.list()
        self.assertIsInstance(lst, list)
        self.assertEqual(len(lst), 10)
        self.assertIsInstance(lst[0], self.cin.movie)
        self.assertEqual(lst[0].id, 131001)

    @activate
    def test_movie_search(self):
        register_uri(GET,
                     rr['movie.search']['req'],
                     body=rr['movie.search']['resp'])
        lst = self.cin.movie.search(u'Пираты кариб')
        self.assertIsInstance(lst, list)
        self.assertEqual(len(lst), 6)
        self.assertIsInstance(lst[0], self.cin.movie)
        self.assertEqual(lst[0].id, 120787)

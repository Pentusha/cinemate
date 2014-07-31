# coding=utf-8
"""
    Модуль содержит запросы и сохранённые ответы сервера для тестирования.
"""
from requests.status_codes import codes
from six import u


account_auth = u('{"passkey": "of3k4oasd9498dfvjh5hthhgfgdfy"}')
account_profile = u('{"username": "UserName", "reputation": 125, "review_count": 11, "gold_badges": 2, "silver_badges": 14, "bronze_badges": 21, "unread_pm_count": 3, "unread_forum_count": 7, "unread_updatelist_count": 2, "subscription_count": 96}')  # noqa
account_updatelist = u('{"item": [{"date": "2011-04-09T15:38:30", "description": "Новая раздача", "url": "http://cinemate.cc/watchlist/a415ef22a4b7ebf24bc54d7ad9a92fa4612cb49f/read/400813/", "new": 1, "for_object": {"movie": {"id": 115866, "title": "Элизиум: Рай не на Земле (2013)"}}}, {"date": "2011-04-09T15:28:35", "description": "2 новых комментария", "url": "http://cinemate.cc/watchlist/a415ef22a4b7ebf24bc54d7ad9a92fa4612cb49f/read/400812:400811/", "new": 0, "for_object": {"comment": {"id": 1810, "title": "Отзыв admin на фильм «Красное на белом (2009)»"}}}, {"date": "2011-04-09T15:27:24", "description": "Новый фильм", "url": "http://cinemate.cc/watchlist/a415ef22a4b7ebf24bc54d7ad9a92fa4612cb49f/read/400742:400743/", "new": 0, "for_object": {"person": {"id": 830, "title": "Райан Гослинг"}}}, {"date": "2011-04-09T15:17:14", "description": "3 новых раздачи", "url": "http://cinemate.cc/watchlist/a415ef22a4b7ebf24bc54d7ad9a92fa4612cb49f/read/400601:400599:400598/", "new": 0, "for_object": {"movie": {"id": 115866, "title": "Элизиум: Рай не на Земле (2013)"}}}]}')  # noqa
account_watchlist = u('{"comment": [{"date": "2011-04-09T15:38:30", "name": "Отзыв UserName на фильм «Назад в будущее (1985)»", "description": "Новые комментарии", "url": "http://cinemate.cc/comment/123/"}, {"date": "2011-04-09T15:28:35", "name": "Отзыв UserName на фильм «Пипец (2010)»", "description": "Новые комментарии", "url": "http://cinemate.cc/comment/456/"}], "person": [{"date": "2011-04-02T02:08:23", "name": "Лив Тайлер", "description": "Новые фильмы с участием", "url": "http://cinemate.cc/person/18104/"}, {"date": "2011-04-03T02:08:31", "name": "Кристен Стюарт", "description": "Новые фильмы с участием", "url": "http://cinemate.cc/person/8151/"}], "movie": [{"date": "2011-04-04T16:37:24", "name": "Кунг-фу Панда 2 (2011)", "description": "Новые раздачи", "url": "http://cinemate.cc/movie/68725/"}, {"date": "2011-04-07T16:37:27", "name": "Супер 8 (2011)", "description": "Новые раздачи", "url": "http://cinemate.cc/movie/68709/"}]}')  # noqa
movie = u('{"movie": {"kinopoisk": {"rating": "6.2", "votes": "11673"}, "director": {"person": {"attrib": {"id": "163239"}, "value": "Малькольм Венвилль"}}, "description": "Встречайте Генри – самого унылого парня в Америке. Он сидит в своей будке у дороги, взимая пошлину с проезжающих. Казалось, в его жизни ничто не может измениться. Но однажды сомнительный приятель попросил Генри подождать его у крыльца главного банка в Буффало... В результате – четыре года тюрьмы по ложному обвинению в ограблении. Но пройдет время, и Генри вернется к тому самому банку, чтобы взять свое…", "url": "http://cinemate.cc/movie/68675/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2010/68675/1298810716.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2010/68675/1298810716.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2010/68675/1298810716.medium.jpg"}}, "release_date_russia": "2011-04-07", "title_original": "Henry\'s Crime", "country": {"name": "США"}, "cast": {"person": [{"attrib": {"id": "2624"}, "value": "Киану Ривз"}, {"attrib": {"id": "1219"}, "value": "Вера Фармига"}, {"attrib": {"id": "2856"}, "value": "Петер Стормаре"}, {"attrib": {"id": "112"}, "value": "Джеймс Каан"}, {"attrib": {"id": "2243"}, "value": "Джуди Грир"}, {"attrib": {"id": "9803"}, "value": "Билл Дьюк"}, {"attrib": {"id": "13257"}, "value": "Фишер Стивенс"}, {"attrib": {"id": "39646"}, "value": "Карри Грэм"}, {"attrib": {"id": "9040"}, "value": "Дэвид Костабайл"}, {"attrib": {"id": "5933"}, "value": "Дэнни Хоч"}, {"attrib": {"id": "67860"}, "value": "Хэзер МакРэй"}, {"attrib": {"id": "108757"}, "value": "Джордан Гелбер"}, {"attrib": {"id": "190286"}, "value": "Елена Беука"}, {"attrib": {"id": "148348"}, "value": "Сара Гленденинг"}, {"attrib": {"id": "190285"}, "value": "Жули Ордон"}]}, "imdb": {"rating": "5.9", "votes": "12147"}, "title_russian": "Криминальная фишка от Генри", "year": 2010, "genre": {"name": "комедия"}, "runtime": 108, "type": "movie", "id": 68675, "trailer": "http://www.youtube.com/watch?v=6IcqfNeql68", "release_date_world": "2011-04-07"}}')  # noqa
movie_one_person = u('{"movie": {"kinopoisk": {"rating": "8.1", "votes": "254"}, "director": {"person": [{"attrib": {"id": "82691"}, "value": "Джозеф Барбера"}, {"attrib": {"id": "82697"}, "value": "Уильям Ханна"}]}, "release_date_world": "1944-04-14", "description": "Том и Джерри вызывают смех и покоряют сердца детей и взрослых всего мира на протяжении десятилетий. Эти герои поражают зрителей своим мастерством перевоплощения, изобретательными трюками и розыгрышами, изощренными ловушками и уморительными проделками.", "url": "http://cinemate.cc/movie/147668/", "poster": {"small": {"url": "http://c.cinemate.cc/media/m/8/6/147668/0_2.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/m/8/6/147668/0_2.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/m/8/6/147668/0_2.medium.jpg"}}, "title_english": "Tom and Jerry", "country": {"name": "США"}, "cast": {"person": {"attrib": {"id": "82697"}, "value": "Уильям Ханна"}}, "imdb": {"rating": "7.3", "votes": "384"}, "title_original": "The Million Dollar Cat", "year": 1944, "genre": {"name": ["комедия", "короткометражка", "мультфильм", "семейный"]}, "runtime": 7, "type": "short", "id": 147668, "title_russian": "Кот на миллион долларов"}}')  # noqa
movie_list = u('{"movie": [{"url": "http://cinemate.cc/movie/131001/", "poster": {"small": {"url": "http://c.cinemate.cc/media/m/1/0/131001/0.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/m/1/0/131001/0.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/m/1/0/131001/0.medium.jpg"}}, "title_original": "Mike & Molly", "title_russian": "Майк и Молли", "year": 2010, "runtime": 30, "type": "serial", "id": 131001}, {"url": "http://cinemate.cc/movie/131657/", "poster": {"small": {"url": "http://c.cinemate.cc/media/m/7/5/131657/0.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/m/7/5/131657/0.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/m/7/5/131657/0.medium.jpg"}}, "title_original": "Astonishing X-Men: Gifted", "title_russian": "Удивительные Люди Икс: Одаренные", "year": 2010, "runtime": 60, "type": "video", "id": 131657}, {"url": "http://cinemate.cc/movie/109767/", "poster": {"small": {"url": "http://c.cinemate.cc/media/m/7/6/109767/0_1.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/m/7/6/109767/0_1.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/m/7/6/109767/0_1.medium.jpg"}}, "title_original": "Iron Man: Extremis", "title_russian": "Железный человек: Экстремис", "year": 2010, "runtime": 0, "type": "serial", "id": 109767}, {"url": "http://cinemate.cc/movie/83460/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2010/83460/1317311479.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2010/83460/1317311479.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2010/83460/1317311479.medium.jpg"}}, "title_original": "America", "title_russian": "Америка", "year": 2010, "runtime": 111, "type": "movie", "id": 83460}, {"url": "http://cinemate.cc/movie/66450/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2010/66450/1293283029.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2010/66450/1293283029.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2010/66450/1293283029.medium.jpg"}}, "title_original": "Autoreiji", "title_russian": "Беспредел", "year": 2010, "runtime": 110, "type": "movie", "id": 66450}, {"url": "http://cinemate.cc/movie/135826/", "poster": {"small": {"url": "http://c.cinemate.cc/media/m/6/2/135826/0.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/m/6/2/135826/0.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/m/6/2/135826/0.medium.jpg"}}, "title_original": "Making History", "title_russian": "Воссоздавая историю", "year": 2010, "runtime": 50, "type": "serial", "id": 135826}, {"url": "http://cinemate.cc/movie/105524/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2010/105524/1353677755.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2010/105524/1353677755.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2010/105524/1353677755.medium.jpg"}}, "title_original": "High School", "title_russian": "Крутые кексы", "year": 2010, "runtime": 99, "type": "movie", "id": 105524}, {"url": "http://cinemate.cc/movie/122874/", "poster": {"small": {"url": "http://c.cinemate.cc/media/m/4/7/122874/0.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/m/4/7/122874/0.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/m/4/7/122874/0.medium.jpg"}}, "title_original": "The Big C", "title_russian": "Большая буква «Р»", "year": 2010, "runtime": 28, "type": "serial", "id": 122874}, {"url": "http://cinemate.cc/movie/133159/", "poster": {"small": {"url": "http://c.cinemate.cc/media/m/9/5/133159/0_2.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/m/9/5/133159/0_2.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/m/9/5/133159/0_2.medium.jpg"}}, "title_original": "Killing Time", "title_russian": "Час Икс", "year": 2010, "runtime": 60, "type": "serial", "id": 133159}, {"url": "http://cinemate.cc/movie/52036/", "poster": {"small": {"url": "http://c.cinemate.cc/media/m/6/3/52036/0.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/m/6/3/52036/0.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/m/6/3/52036/0.medium.jpg"}}, "title_original": "Legend of the Boneknapper Dragon", "title_russian": "Легенда о Костоломе", "year": 2010, "runtime": 16, "type": "short", "id": 52036}]}')  # noqa
movie_list_with_params = u('{"movie": [{"kinopoisk": {"rating": "7.6", "votes": "1618"}, "url": "http://cinemate.cc/movie/24424/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/1989/24424/1377737418.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/1989/24424/1377737418.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/1989/24424/1377737418.medium.jpg"}}, "title_original": "Don Sezar de Bazan", "imdb": {"rating": "7.2", "votes": "137"}, "title_russian": "Дон Сезар де Базан", "year": 1989, "runtime": 133, "type": "movie", "id": 24424}, {"kinopoisk": {"rating": "6.9", "votes": "730"}, "url": "http://cinemate.cc/movie/6685/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/1988/6685/1292319867.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/1988/6685/1292319867.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/1988/6685/1292319867.medium.jpg"}}, "title_original": "Tetsuo, the Iron Man", "imdb": {"rating": "7.0", "votes": "11508"}, "title_russian": "Тетсуо - железный человек", "year": 1988, "runtime": 67, "type": "movie", "id": 6685}, {"url": "http://cinemate.cc/movie/114718/", "poster": {"small": {"url": "http://c.cinemate.cc/media/m/8/1/114718/0.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/m/8/1/114718/0.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/m/8/1/114718/0.medium.jpg"}}, "title_original": "Bad Blood", "imdb": {"rating": "5.3", "votes": "61"}, "title_russian": "Дурная кровь", "year": 1989, "runtime": 104, "type": "movie", "id": 114718}, {"kinopoisk": {"rating": "5.4", "votes": "17"}, "url": "http://cinemate.cc/movie/32660/", "poster": {"small": {"url": "http://c.cinemate.cc/media/m/0/6/32660/0.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/m/0/6/32660/0.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/m/0/6/32660/0.medium.jpg"}}, "title_original": "The Evil Below", "imdb": {"rating": "3.0", "votes": "113"}, "title_russian": "Зло из бездны", "year": 1989, "runtime": 92, "type": "movie", "id": 32660}, {"url": "http://cinemate.cc/movie/117681/", "poster": {"small": {"url": "http://c.cinemate.cc/media/m/1/8/117681/0.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/m/1/8/117681/0.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/m/1/8/117681/0.medium.jpg"}}, "title_original": "Beach Fever", "imdb": {"rating": "4.0", "votes": "61"}, "title_russian": "Пляжная лихорадка", "year": 1987, "runtime": 90, "type": "movie", "id": 117681}, {"kinopoisk": {"rating": "6.0", "votes": "14"}, "url": "http://cinemate.cc/movie/38105/", "poster": {"small": {"url": "http://c.cinemate.cc/media/m/5/0/38105/0.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/m/5/0/38105/0.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/m/5/0/38105/0.medium.jpg"}}, "title_original": "Slunce, seno a pár facek", "imdb": {"rating": "6.9", "votes": "483"}, "title_russian": "Солнце, сено и пара оплеух", "year": 1989, "runtime": 128, "type": "movie", "id": 38105}, {"kinopoisk": {"rating": "6.3", "votes": "149"}, "url": "http://cinemate.cc/movie/18319/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/1989/18319/1377445993.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/1989/18319/1377445993.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/1989/18319/1377445993.medium.jpg"}}, "title_original": "Far from Home", "imdb": {"rating": "5.7", "votes": "1106"}, "title_russian": "Вдали от дома", "year": 1989, "runtime": 86, "type": "movie", "id": 18319}, {"kinopoisk": {"rating": "6.1", "votes": "1134"}, "url": "http://cinemate.cc/movie/7139/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/1989/7139/1292319718.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/1989/7139/1292319718.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/1989/7139/1292319718.medium.jpg"}}, "title_original": "The Karate Kid, Part III", "imdb": {"rating": "4.8", "votes": "23707"}, "title_russian": "Парень-каратист 3", "year": 1989, "runtime": 112, "type": "movie", "id": 7139}, {"kinopoisk": {"rating": "7.5", "votes": "449"}, "url": "http://cinemate.cc/movie/14832/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/1989/14832/1292319378.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/1989/14832/1292319378.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/1989/14832/1292319378.medium.jpg"}}, "title_original": "Great Balls of Fire!", "imdb": {"rating": "6.1", "votes": "10631"}, "title_russian": "Большие огненные шары", "year": 1989, "runtime": 108, "type": "movie", "id": 14832}, {"kinopoisk": {"rating": "5.9", "votes": "56"}, "url": "http://cinemate.cc/movie/19272/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/1989/19272/1377487523.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/1989/19272/1377487523.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/1989/19272/1377487523.medium.jpg"}}, "title_original": "Curse II: The Bite", "imdb": {"rating": "4.6", "votes": "508"}, "title_russian": "Проклятие 2: Укус", "year": 1989, "runtime": 98, "type": "movie", "id": 19272}]}')  # noqa
movie_search = u('{"movie": [{"url": "http://cinemate.cc/movie/120787/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2015/120787/1376572594.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2015/120787/1376572594.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2015/120787/1376572594.medium.jpg"}}, "title_original": "Pirates of the Caribbean: Dead Men Tell No Tales", "title_russian": "Пираты Карибского моря: Мертвецы не рассказывают сказки", "year": 2016, "runtime": 0, "type": "movie", "id": 120787}, {"url": "http://cinemate.cc/movie/68669/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2011/68669/1302893688.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2011/68669/1302893688.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2011/68669/1302893688.medium.jpg"}}, "title_original": "Pirates of the Caribbean: On Stranger Tides", "title_russian": "Пираты Карибского моря: На странных берегах", "year": 2011, "runtime": 141, "type": "movie", "id": 68669}, {"url": "http://cinemate.cc/movie/1787/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2007/1787/1292319730.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2007/1787/1292319730.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2007/1787/1292319730.medium.jpg"}}, "title_original": "Pirates of the Caribbean: At World\'s End", "title_russian": "Пираты Карибского моря 3: На краю Света", "year": 2007, "runtime": 169, "type": "movie", "id": 1787}, {"url": "http://cinemate.cc/movie/2194/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2006/2194/1292319730.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2006/2194/1292319730.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2006/2194/1292319730.medium.jpg"}}, "title_original": "Pirates of the Caribbean: Dead Man\'s Chest", "title_russian": "Пираты Карибского моря 2: Сундук мертвеца", "year": 2006, "runtime": 151, "type": "movie", "id": 2194}, {"url": "http://cinemate.cc/movie/15869/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2006/15869/1326444121.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2006/15869/1326444121.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2006/15869/1326444121.medium.jpg"}}, "title_original": "Blackbeard: Terror at Sea", "title_russian": "Пираты карибского моря: Черная борода", "year": 2006, "runtime": 120, "type": "movie", "id": 15869}, {"url": "http://cinemate.cc/movie/7412/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2003/7412/1292319730.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2003/7412/1292319730.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2003/7412/1292319730.medium.jpg"}}, "title_original": "Pirates of the Caribbean: The Curse of the Black Pearl", "title_russian": "Пираты Карибского моря: Проклятие черной жемчужины", "year": 2003, "runtime": 143, "type": "movie", "id": 7412}]}')  # noqa
person = u('{"person": {"url": "http://cinemate.cc/person/3971/", "photo": {"small": {"url": "http://c.cinemate.cc/media/images/photo/j/3971/1290595484.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/photo/j/3971/1290595484.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/photo/j/3971/1290595484.medium.jpg"}}, "name_original": "Jake Gyllenhaal", "id": 3971, "name": "Джейк Джилленхол"}}')  # noqa
person_movies = u('{"person": {"name": "Ян Шванкмайер", "url": "http://cinemate.cc/person/43083/", "photo": {"small": {"url": "http://c.cinemate.cc/media/images/photo/j/43083/1370195170.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/photo/j/43083/1370195170.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/photo/j/43083/1370195170.medium.jpg"}}, "name_original": "Jan Svankmajer", "movies": {"director": {"movie": [{"kinopoisk": {"rating": "7.8", "votes": "378"}, "url": "http://cinemate.cc/movie/79144/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2010/79144/1337584424.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2010/79144/1337584424.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2010/79144/1337584424.medium.jpg"}}, "title_original": "Prezít svuj zivot (teorie a praxe)", "imdb": {"rating": "7.3", "votes": "575"}, "title_russian": "Пережить свою жизнь", "year": 2010, "runtime": 105, "type": "movie", "id": 79144}, {"kinopoisk": {"rating": "7.4", "votes": "1361"}, "url": "http://cinemate.cc/movie/4974/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2005/4974/1371138631.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2005/4974/1371138631.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2005/4974/1371138631.medium.jpg"}}, "title_original": "Lunacy", "imdb": {"rating": "7.3", "votes": "2140"}, "title_russian": "Безумие", "year": 2005, "runtime": 123, "type": "movie", "id": 4974}, {"kinopoisk": {"rating": "7.5", "votes": "2248"}, "url": "http://cinemate.cc/movie/31965/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2000/31965/1342179109.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2000/31965/1342179109.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2000/31965/1342179109.medium.jpg"}}, "title_original": "Otesánek", "imdb": {"rating": "7.3", "votes": "3988"}, "title_russian": "Полено", "year": 2000, "runtime": 132, "type": "movie", "id": 31965}, {"kinopoisk": {"rating": "7.7", "votes": "904"}, "url": "http://cinemate.cc/movie/4703/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/1996/4703/1292319567.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/1996/4703/1292319567.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/1996/4703/1292319567.medium.jpg"}}, "title_original": "Conspirators of Pleasure", "imdb": {"rating": "7.6", "votes": "1856"}, "title_russian": "Конспираторы наслаждений", "year": 1996, "runtime": 75, "type": "movie", "id": 4703}, {"kinopoisk": {"rating": "7.4", "votes": "471"}, "url": "http://cinemate.cc/movie/5509/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/1994/5509/1335564018.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/1994/5509/1335564018.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/1994/5509/1335564018.medium.jpg"}}, "title_original": "Faust", "imdb": {"rating": "7.5", "votes": "2298"}, "title_russian": "Урок Фауста", "year": 1994, "runtime": 97, "type": "movie", "id": 5509}]}, "actor": {"movie": [{"kinopoisk": {"rating": "7.8", "votes": "378"}, "url": "http://cinemate.cc/movie/79144/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2010/79144/1337584424.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2010/79144/1337584424.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2010/79144/1337584424.medium.jpg"}}, "title_original": "Prezít svuj zivot (teorie a praxe)", "imdb": {"rating": "7.3", "votes": "575"}, "title_russian": "Пережить свою жизнь", "year": 2010, "runtime": 105, "type": "movie", "id": 79144}, {"kinopoisk": {"rating": "7.4", "votes": "1361"}, "url": "http://cinemate.cc/movie/4974/", "poster": {"small": {"url": "http://c.cinemate.cc/media/images/poster/2005/4974/1371138631.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/poster/2005/4974/1371138631.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/poster/2005/4974/1371138631.medium.jpg"}}, "title_original": "Lunacy", "imdb": {"rating": "7.3", "votes": "2140"}, "title_russian": "Безумие", "year": 2005, "runtime": 123, "type": "movie", "id": 4974}]}}, "id": 43083}}')  # noqa
person_search = u('{"person": [{"url": "http://cinemate.cc/person/3971/", "photo": {"small": {"url": "http://c.cinemate.cc/media/images/photo/j/3971/1290595484.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/photo/j/3971/1290595484.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/photo/j/3971/1290595484.medium.jpg"}}, "name_original": "Jake Gyllenhaal", "id": 3971, "name": "Джейк Джилленхол"}, {"url": "http://cinemate.cc/person/1685/", "photo": {"small": {"url": "http://c.cinemate.cc/media/images/photo/m/1685/1290595500.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/photo/m/1685/1290595500.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/photo/m/1685/1290595500.medium.jpg"}}, "name_original": "Maggie Gyllenhaal", "id": 1685, "name": "Мэгги Джилленхол"}, {"url": "http://cinemate.cc/person/79826/", "photo": {"small": {"url": "http://c.cinemate.cc/media/images/photo/s/79826/1378045945.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/photo/s/79826/1378045945.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/photo/s/79826/1378045945.medium.jpg"}}, "name_original": "Stephen Gyllenhaal", "id": 79826, "name": "Стивен Джилленхол"}, {"url": "http://cinemate.cc/person/76362/", "photo": {"small": {"url": "http://c.cinemate.cc/media/images/photo/e/76362/1377305848.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/photo/e/76362/1377305848.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/photo/e/76362/1377305848.medium.jpg"}}, "name_original": "Eric Mendenhall", "id": 76362, "name": "Эрик Менденхол"}, {"url": "http://cinemate.cc/person/361603/", "photo": {"small": {"url": "http://c.cinemate.cc/media/images/photo/blank.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/photo/blank.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/photo/blank.medium.jpg"}}, "name_original": "Мэгги Джилленхол", "id": 361603, "name": "Мэгги Джилленхол"}, {"url": "http://cinemate.cc/person/303647/", "photo": {"small": {"url": "http://c.cinemate.cc/media/images/photo/blank.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/photo/blank.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/photo/blank.medium.jpg"}}, "name_original": "Stephen Gyllenhaal", "id": 303647, "name": "Стивен Джилленхол"}, {"url": "http://cinemate.cc/person/333519/", "photo": {"small": {"url": "http://c.cinemate.cc/media/images/photo/blank.small.jpg"}, "big": {"url": "http://c.cinemate.cc/media/images/photo/blank.big.jpg"}, "medium": {"url": "http://c.cinemate.cc/media/images/photo/blank.medium.jpg"}}, "name_original": "Стивен Джилленхол", "id": 333519, "name": "Стивен Джилленхол"}]}')  # noqa
stats_new = u('{"users_count": 4, "reviews_count": 0, "comments_count": 2, "movies_count": 7}')  # noqa
stats_wtf = u('{"error": "Unknown error"}')
response404 = u('response irrelevant 404')


reqresp = {
    'account.auth': {
        'cmd': 'account.auth',
        'params': {
            'username': 'USERNAME',
            'password': 'PASSWORD',
        },
        'body': account_auth,
    },
    'account.profile': {
        'cmd': 'account.profile',
        'params': {
            'passkey': 'PASSKEY',
        },
        'body': account_profile,
    },
    'account.updatelist': {
        'cmd': 'account.updatelist',
        'params': {
            'passkey': 'PASSKEY',
            'newonly': 1,
        },
        'body': account_updatelist,
    },
    'account.watchlist': {
        'cmd': 'account.watchlist',
        'params': {
            'passkey': 'PASSKEY',
        },
        'body': account_watchlist,
    },
    'movie': {
        'cmd': 'movie',
        'params': {
            'apikey': 'APIKEY',
            'id': 68675,
        },
        'body': movie,
    },
    'movie_one_person': {
        'cmd': 'movie',
        'params': {
            'apikey': 'APIKEY',
            'id': 147668,
        },
        'body': movie_one_person,
    },
    'movie.list': {
        'cmd': 'movie.list',
        'params': {
            'apikey': 'APIKEY',
            'year': 2010,
        },
        'body': movie_list,
    },
    'movie.list_with_params': {
        'cmd': 'movie.list',
        'params': {
            'apikey': 'APIKEY',
            'to': '04.07.1989',
            'from': '04.07.1988',
            'order_by': 'release_date',
        },
        'body': movie_list_with_params,
    },
    'movie.search': {
        'cmd': 'movie.search',
        'params': {
            'apikey': 'APIKEY',
            'term': u('Пираты%20кариб'),
        },
        'body': movie_search,
    },
    'person': {
        'cmd': 'person',
        'params': {
            'id': 3971,
            'apikey': 'APIKEY',
        },
        'body': person,
    },
    'person.movies': {
        'cmd': 'person.movies',
        'params': {
            'id': 43083,
            'apikey': 'APIKEY',
        },
        'body': person_movies,
    },
    'person.search': {
        'cmd': 'person.search',
        'params': {
            'apikey': 'APIKEY',
            'term': u('гиленхол'),
        },
        'body': person_search,
    },
    'stats.new': {
        'cmd': 'stats.new',
        'params': {},
        'body': stats_new,
    },
    'stats.wtf': {  # raise RuntimeError('Unknown error')
        'cmd': 'stats.wtf',
        'params': {},
        'body': stats_wtf,
    },
    'account.wrong_status_code': {  # raise RuntimeError()
        'cmd': 'account.auth',
        'params': {
            'username': 'USERNAME',
            'password': 'PASSWORD',
            'format': 'pewpewpew',
        },
        'body': response404,
        'status': codes.not_found,
    },
}

base_url = 'http://api.cinemate.cc/'
for key, value in reqresp.items():
    value['params'].setdefault('format', 'json')
    reqresp[key]['uri'] = u('{base}{cmd}?{params}').format(
        base=base_url,
        cmd=value['cmd'],
        params='&'.join(u('{}={}').format(k, v) for k, v in value.items())
    )
    del value['params']
    del value['cmd']

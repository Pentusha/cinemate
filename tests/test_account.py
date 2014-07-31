# coding=utf-8
from datetime import datetime

import pytest
from pytest_httpretty import stub_get
from six import u


@pytest.mark.httpretty
def test_auth(cin, rr):
    stub_get(**rr['account.auth'])
    cin.account.auth()
    assert cin.passkey == 'of3k4oasd9498dfvjh5hthhgfgdfy'


@pytest.mark.httpretty
def test_profile(cin, rr):
    stub_get(**rr['account.profile'])
    profile = cin.account.profile()
    assert isinstance(profile, dict)
    assert profile == {
        'username': 'UserName',
        'reputation': 125,
        'review_count': 11,
        'gold_badges': 2,
        'silver_badges': 14,
        'bronze_badges': 21,
        'unread_pm_count': 3,
        'unread_forum_count': 7,
        'unread_updatelist_count': 2,
        'subscription_count': 96,
    }


@pytest.mark.httpretty
def test_updatelist(cin, rr):
    stub_get(**rr['account.updatelist'])
    lst = cin.account.updatelist()
    first = lst[0]
    assert isinstance(lst, list)
    assert len(lst) == 4
    assert isinstance(first, dict)
    assert first['date'] == datetime(2011, 4, 9, 15, 38, 30)
    assert isinstance(first['for_object'], cin.movie)
    assert first['description'] == u('Новая раздача')
    assert first['url'] == (
        'http://cinemate.cc/watchlist/'
        'a415ef22a4b7ebf24bc54d7ad9a92fa4612cb49f/read/400813/'
    )
    assert first['new'] == 1


@pytest.mark.httpretty
def test_watchlist(cin, rr):
    stub_get(**rr['account.watchlist'])
    wlst = cin.account.watchlist()
    assert isinstance(wlst, dict)
    assert 'movie' in wlst
    assert 'person' in wlst
    assert isinstance(wlst['movie'], list)
    assert isinstance(wlst['person'], list)
    assert len(wlst['movie']) == 2
    assert len(wlst['person']) == 2
    movie = wlst['movie'][0]
    assert isinstance(movie, cin.movie)
    person = wlst['person'][0]
    assert isinstance(person, cin.person)

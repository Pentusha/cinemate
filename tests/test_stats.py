# coding=utf-8
import pytest
from pytest_httpretty import stub_get


@pytest.mark.httpretty
def test_new(cin, rr):
    stub_get(**rr['stats.new'])
    stats = cin.stats.new()
    assert stats == {
        'users_count': 4,
        'reviews_count': 0,
        'comments_count': 2,
        'movies_count': 7,
    }

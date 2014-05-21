# coding=utf-8
import pytest
from pytest_httpretty import stub_get
from .mock import reqresp as rr


@pytest.mark.httpretty
def test_new(cin):
    stub_get(**rr['stats.new'])
    stats = cin.stats.new()
    assert isinstance(stats, dict)
    assert 'users_count' in stats
    assert isinstance(stats['users_count'], int)
    assert stats['users_count'] == 4
    assert 'reviews_count' in stats
    assert isinstance(stats['reviews_count'], int)
    assert stats['reviews_count'] == 0
    assert 'comments_count' in stats
    assert isinstance(stats['comments_count'], int)
    assert stats['comments_count'] == 2
    assert 'movies_count' in stats
    assert isinstance(stats['movies_count'], int)
    assert stats['movies_count'] == 7

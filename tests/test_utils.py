# coding=utf-8
from datetime import datetime
import pytest

from cinemate import utils


@pytest.mark.parametrize(
    'iso_input, expected',
    (
        ('', None),
        (None, None),
        ('2011-04-09T15:38:30', datetime(2011, 4, 9, 15, 38, 30)),
        ('2015-01-22T02:14:00', datetime(2015, 1, 22, 2, 14, 0)),
    )
)
def test_parse_datetime(iso_input, expected):
    assert utils.parse_datetime(iso_input) == expected


@pytest.mark.parametrize(
    'iso_input, expected',
    (
        ('', None),
        (None, None),
        ('2011-04-07', datetime(2011, 4, 7)),
        ('2015-01-22', datetime(2015, 1, 22)),
    )
)
def test_parse_date(iso_input, expected):
    assert utils.parse_date(iso_input) == expected


def test_required(cin):
    dummy = type('Dummy', (object,), {
        'cinemate': cin,
        'decorated': utils.require('test')(lambda: None)
    })
    with pytest.raises(AttributeError):
        dummy().decorated()


def test_get_cinemate(cin):
    dummy1 = type('Cinemate', (object,), {})
    dummy2 = type('Dummy', (object,), {'cinemate': cin})
    dummy3 = type('Mummy', (object,), {})
    try:
        utils.__get_cinemate__(dummy1())
    except AttributeError:
        assert False, 'Dummy1 raises AttributeError'
    try:
        utils.__get_cinemate__(dummy2())
    except AttributeError:
        assert False, 'Dummy2 raises AttributeError'
    with pytest.raises(AttributeError):
        utils.__get_cinemate__(dummy3())

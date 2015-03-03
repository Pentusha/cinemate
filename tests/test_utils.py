# coding=utf-8
import pytest
from datetime import datetime
from mock import patch
from cinemate import utils


def test_config_load(mock_config):
    assert getattr(mock_config, '_auth') == {
        'username': 'MOCK_USERNAME',
        'password': 'MOCK_PASSWORD',
        'passkey': 'MOCK_PASSKEY',
        'apikey': 'MOCK_APIKEY',
    }


@patch('cinemate.utils._open')
def test_config_save(open_mock, mock_config):
    mock_config.save()
    open_mock.assert_called_once_with(mock_config.filename, 'w')


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
    foo = type('Foo', (object,), {
        'cinemate': cin,
        'decorated': utils.require('test')(lambda: None)
    })
    bar = type('Bar', (object,), {
        'decorated': utils.require('test')(lambda: None)
    })
    with pytest.raises(AttributeError):
        foo().decorated()
    with pytest.raises(AttributeError):
        bar().decorated()

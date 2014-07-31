# coding=utf-8
import pytest
from mock import patch
from pytest_httpretty import stub_get
from requests.status_codes import codes
from cinemate import Cinemate
from .conftest import ContextualStringIO


def test_str(cin):
    assert str(cin) == '<Cinemate: USERNAME>'


@patch('cinemate.utils._exists')
@patch('cinemate.utils._open')
def test_cinemate_wo_params(open_mock, exists_mock, config_content):
    open_mock.return_value = ContextualStringIO(config_content)
    exists_mock.return_value = True
    cin = Cinemate()
    assert cin.username == 'MOCK_USERNAME'
    assert cin.password == 'MOCK_PASSWORD'
    assert cin.passkey == 'MOCK_PASSKEY'
    assert cin.apikey == 'MOCK_APIKEY'


@patch('cinemate.utils._exists')
def test_cinemate_raise_wo_params(exists_mock):
    exists_mock.return_value = False
    with pytest.raises(IOError):
        Cinemate()


@pytest.mark.httpretty
def test_api_get(cin, rr):
    correct_url = 'stats.new'
    incorect_url = 'stats.wtf'
    wrong_status_url = 'account.wrong_status_code'
    stub_get(**rr[correct_url])
    stub_get(**rr[incorect_url])
    stub_get(**rr[wrong_status_url])
    req = cin.api_get(correct_url)
    assert req.status_code == codes.ok
    assert 'error' not in req.json()
    with pytest.raises(RuntimeError):
        cin.api_get(incorect_url)
    not_found_url = rr[wrong_status_url]['uri']
    with pytest.raises(RuntimeError):
        cin.api_get(not_found_url)

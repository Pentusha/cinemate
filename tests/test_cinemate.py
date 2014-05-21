# coding=utf-8
import pytest
from pytest_httpretty import stub_get
from requests.status_codes import codes

from tests.mock import reqresp as rr


def test_str(cin):
    assert str(cin) == '<Cinemate: USERNAME>'


@pytest.mark.httpretty
def test_api_get(cin):
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

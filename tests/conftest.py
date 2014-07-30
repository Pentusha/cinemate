import pytest
from six import StringIO
from mock import patch
from cinemate import Cinemate
from cinemate.utils import CinemateConfig
from .data import reqresp


@pytest.fixture
def cin():
    return Cinemate(
        username='USERNAME',
        password='PASSWORD',
        passkey='PASSKEY',
        apikey='APIKEY',
    )


@pytest.fixture
def rr():
    return reqresp


@pytest.fixture
@patch('cinemate.utils._open')
def fake_config(open_mock):
    open_mock.return_value = StringIO(
        'auth:\n'
        '  username: TEST_USERNAME\n'
        '  password: TEST_PASSWORD\n'
        '  passkey: TEST_PASSKEY\n'
        '  apikey: TEST_APIKEY\n'
    )
    return CinemateConfig()

import pytest
from six import StringIO
from mock import patch
from cinemate import Cinemate
from cinemate.utils import CinemateConfig
from .data import reqresp


class ContextualStringIO(StringIO):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
        return False


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
def config_content():
    return (
        'auth:\n'
        '  username: MOCK_USERNAME\n'
        '  password: MOCK_PASSWORD\n'
        '  passkey: MOCK_PASSKEY\n'
        '  apikey: MOCK_APIKEY\n'
    )


@pytest.fixture
@patch('cinemate.utils._exists')
@patch('cinemate.utils._open')
def mock_config(open_mock, exists_mock, config_content):
    open_mock.return_value = ContextualStringIO(config_content)
    exists_mock.return_value = True
    return CinemateConfig()

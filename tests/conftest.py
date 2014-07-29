import pytest
from cinemate import Cinemate
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

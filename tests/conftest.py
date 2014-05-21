import pytest
from cinemate import Cinemate


@pytest.fixture
def cin():
    return Cinemate(
        username='USERNAME',
        password='PASSWORD',
        passkey='PASSKEY',
        apikey='APIKEY',
    )

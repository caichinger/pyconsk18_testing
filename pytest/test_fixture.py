import pytest

@pytest.fixture
def data():
    return 'We need that'

def test_needs(data):
    assert data == 'Do we need that?'
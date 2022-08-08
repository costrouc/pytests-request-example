import requests
import pytest


@pytest.fixture
def client():
    session = requests.Session()
    yield session

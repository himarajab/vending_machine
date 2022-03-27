import pytest

from pytest_factoryboy import register
from .factories import  UserFactory

register(UserFactory)

@pytest.fixture
def f_user(db, user_factory):
    user = user_factory.create()
    return user
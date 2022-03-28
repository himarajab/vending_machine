import pytest

from pytest_factoryboy import register
from .factories import  UserFactory,SellerFactory,ProductFactory

register(UserFactory)
register(SellerFactory)
register(ProductFactory)

@pytest.fixture
def f_user(db, user_factory):
    user = user_factory.create()
    return user

@pytest.fixture
def f_seller(db, seller_factory):
    seller = seller_factory.create()
    return seller

@pytest.fixture
def f_product(db, product_factory):
    product = product_factory.create()
    return product
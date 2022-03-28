from pprint import pprint
import factory
from django.db.models.signals import post_save
from faker import Faker
from django.contrib.auth import get_user_model
from product.models import Product


User = get_user_model()
fake = Faker()




@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    """
    User factory
    """

    class Meta:
        model = User
        django_get_or_create = ('username',)
    id=1
    username = 'hima'
    deposit=100
    role='buyer'

class SellerFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User
        django_get_or_create = ('username',)
    id=2
    username = 'seller'
    deposit = 0
    role='seller'


class ProductFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Product
        
    id=1
    amount_available = 10
    cost=10
    name='first'
    seller=factory.SubFactory('users.tests.factories.SellerFactory')
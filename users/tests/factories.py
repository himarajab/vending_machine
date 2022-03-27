from pprint import pprint
import factory
from django.db.models.signals import post_save
from faker import Faker
from django.contrib.auth import get_user_model



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
    deposit=0
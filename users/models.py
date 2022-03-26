from django.db import models
from django.contrib.auth.models import AbstractUser

USER_ROLES = (
        ('seller', 'Seller'),
        ('buyer', 'Buyer'),
    )
DEPOSIT_VALUES = (
        (0, 0),
        (5, 5),
        (10, 10),
        (20, 20),
        (50, 50),
        (100, 100),
    )
class User(AbstractUser):
    deposit = models.IntegerField(default=DEPOSIT_VALUES[0], choices=DEPOSIT_VALUES,null=False,blank=False)
    role = models.CharField(max_length=10, choices=USER_ROLES,null=False,blank=False)


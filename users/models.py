from django.db import models
from django.contrib.auth.models import AbstractUser

USER_ROLES = (
        ('seller', 'Seller'),
        ('buyer', 'Buyer'),
    )

class User(AbstractUser):
    deposit = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    role = models.CharField(max_length=10, choices=USER_ROLES,null=False,blank=False)


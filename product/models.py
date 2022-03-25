from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

class Product(models.Model):
    amount_available=models.IntegerField()
    cost=models.DecimalField( max_digits=5, decimal_places=2)
    name=models.CharField(max_length=50)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = ("Product")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})


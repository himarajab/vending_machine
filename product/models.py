from django.db import models

class Product(models.Model):
    seller_id=models.IntegerField()
    amount_available=models.IntegerField()
    cost=models.DecimalField( max_digits=5, decimal_places=2)
    name=models.CharField(max_length=50)
    

    class Meta:
        verbose_name = ("Product")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})


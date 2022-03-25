from ..models import Product
from rest_framework import serializers






class DetailProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "amount_available",
            "cost",
            "name",
            "seller",
        ]
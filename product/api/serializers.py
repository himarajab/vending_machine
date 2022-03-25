from ..models import Product
from rest_framework import serializers



class ProductSerializer(serializers.ModelSerializer):
    cost = serializers.DecimalField(
        max_digits=10, decimal_places=2, coerce_to_string=False
    )
    class Meta:
        model = Product
        fields = ('amount_available', 'cost','name','seller')

    def create(self, validated_data):
        product = Product(**validated_data)
        product.save()
        return product



class DetailProductSerializer(serializers.ModelSerializer):
    cost = serializers.DecimalField(5, 2)
  
    class Meta:
        model = Product
        fields = [
            "id",
            "amount_available",
            "cost",
            "name",
            "seller",
        ]
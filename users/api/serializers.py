from pprint import pprint
from rest_framework import serializers
from django.contrib.auth import get_user_model
from product.models import Product

User=get_user_model()
DEPOSIT_VALUES = (
        ('5', 5),
        ('10', 10),
        ('20', 20),
        ('50', 50),
        ('100', 100),
    )



        
class BuySerializer(serializers.ModelSerializer):
    amount_available = serializers.ReadOnlyField(required=False)
    cost = serializers.ReadOnlyField(required=False)
    name = serializers.ReadOnlyField(required=False)
    seller = serializers.ReadOnlyField(required=False)
    
    def validate(self, attrs):
        pprint(vars(self))
        product = attrs['product_id']
        quantity = attrs['quantity']
  
        product_obj=Product.objects.filter(id=product.pk)
        if product_obj: 
            product_availablequantity =product_obj.first().availablequantity
        else:
            raise serializers.ValidationError({"error": 'product not available now .. '})

        if quantity > product_availablequantity:
            message = {str(product): 'Not available  quantity'}
            error_items.update(message)
        else:
            product_obj.update(availablequantity=F('availablequantity') -requested_quantity)

        return attrs
        

    class Meta:
        model = Product
        fields = [
            "amount_available",
            "cost",
            "name",
            "seller",
            
        ]
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password','role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class DetailUserSerializer(serializers.ModelSerializer):
    pk = serializers.ReadOnlyField(required=False)
    username = serializers.ReadOnlyField(required=False)
    role = serializers.ReadOnlyField(required=False)
    class Meta:
        model = User
        fields = [
            "pk",
            "username",
            "role",
            "deposit",
        ]
from django.db.models import F
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
        product_id = self.context['request'].parser_context['kwargs']['product_id']
        quantity = self.context['request'].parser_context['kwargs']['quantity']
  
        product_obj=Product.objects.filter(id=product_id)
        if product_obj: 
            product_amount_available =product_obj.first().amount_available

        if quantity > product_amount_available:
            message = {str(product_id): 'Not available  quantity'}
            raise serializers.ValidationError({"error": message })
        else:
            product_obj.update(amount_available=F('amount_available') -quantity)

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
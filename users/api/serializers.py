from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model

User=get_user_model()
DEPOSIT_VALUES = (
        ('5', 5),
        ('10', 10),
        ('20', 20),
        ('50', 50),
        ('100', 100),
    )

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
    deposit = serializers.ChoiceField(choices=DEPOSIT_VALUES)
    class Meta:
        model = User
        fields = [
            "pk",
            "username",
            "role",
            "deposit",
        ]
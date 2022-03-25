from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model

User=get_user_model()

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
    username = serializers.ReadOnlyField(required=False)
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "role",
            "role",
            "deposit",
        ]
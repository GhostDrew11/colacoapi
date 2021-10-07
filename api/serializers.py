from rest_framework import serializers
from .models import Order, Soda
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class SodaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soda
        fields = ['id','product_name','description','cost','quantity']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'product_name', 'cost', 'quantity', 'card_number', 'security_code', 'expiration_date', 'zip_code']

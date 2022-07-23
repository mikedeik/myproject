from rest_framework import serializers
from .models import Person, Category, Item, Bidder, Seller, Bid
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'birthdate']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        extra_kwargs = {'password': {'write_only': True,
                                     'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['CategoryId', 'name']


class BidderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bidder
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        bidder = User.objects.create_user(**validated_data)
        Token.objects.create(user=bidder)
        print(bidder.objects)
        return bidder



from dataclasses import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        extra_kwargs = {'username': {'required': True, 'allow_blank': False}}
        extra_kwargs = {'password': {'required': True, 'allow_blank': False}}
        extra_kwargs = {'last_name': {'required': True, 'allow_blank': False}}
        extra_kwargs = {'email': {'required': True, 'allow_blank': False}}

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], first_name=validated_data['first_name'],
                                   last_name=validated_data['last_name'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
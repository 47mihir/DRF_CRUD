from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=50)
    email= serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    role= serializers.CharField(max_length=50)


    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        print(instance.name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        print(instance)
        return instance
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "company_name",
            "phone",
            "type_user",
            "password",

        )

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            company_name=validated_data['company_name'],
            phone=validated_data['phone'],
            type_user=validated_data['type_user']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "company_name",
            "phone",
            "type_user",
        )


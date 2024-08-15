from rest_framework import serializers
from .models import UserModel


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            'user_avatar_url',
            'username',
            'first_name',
            'last_name',
            'email',
            'user_token',
            'user_verify_code',
            'last_login',
            'user_create_date',
            'user_verify_code',
            'is_active',
            'is_superuser',
            'is_staff',
        ]


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            'user_avatar',
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]


class ActiveUserSerializer(serializers.Serializer):
    user_token = serializers.CharField(required=True)
    verify_code = serializers.CharField(required=True, write_only=True)

    class Meta:
        fields = [
            'user_token',
            'verify_code'
        ]


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        fields = [
            'email',
            'password'
        ]


class SendVerifyCodeSerializer(serializers.Serializer):
    user_token = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        fields = [
            'user_token',
            'email'
        ]

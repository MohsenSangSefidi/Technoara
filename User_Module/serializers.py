from rest_framework import serializers
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            'first_name',
            'last_name',
            'email',
            'last_login',
            'user_create_date',
            'is_active',
            'is_superuser',
            'is_staff',
        ]


class RegisterUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        fields = [
            'username',
            'email',
            'password'
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
    email = serializers.EmailField(required=True)

    class Meta:
        fields = [
            'email'
        ]


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    otp = serializers.CharField(required=True)

    class Meta:
        fields = ['email', 'password', 'otp']

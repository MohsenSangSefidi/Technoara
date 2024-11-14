from rest_framework.views import APIView, Response
from rest_framework import status

from django.core.mail import send_mail
from django.conf import settings

from Utils.poll import random_code

from .serializers import (
    UserSerializer, RegisterUserSerializer, LoginUserSerializer, SendVerifyCodeSerializer, ResetPasswordSerializer
)
from .models import TokenModel, OTPModel, UserModel


class GetUserView(APIView):
    def get(self, request, email, *args, **kwargs):
        user = UserModel.objects.filter(email=email).first()

        if user is None:
            return Response({
                'result': False,
                'message': 'کاربری با این ایمیل وجود ندارد.',
                'data': [],
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)
        return Response({
            'result': True,
            'massage': 'کاربر پیدا شد',
            'data': [
                serializer.data
            ]
        })


class RegisterUserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterUserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'result': False,
                'message': 'اطلاعات وارد شده صحیح نیست.',
                'data': [
                    serializer.errors
                ]
            }, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        email = serializer.validated_data.get('email')

        check_user = UserModel.objects.filter(email=email.lower()).first()

        if check_user is not None:
            return Response({
                'result': False,
                'massage': 'کاربری با این ایمیل وجود دارد.',
                'data': []
            }, status=status.HTTP_400_BAD_REQUEST)

        user = UserModel(
            username=username,
            email=email.lower(),
            is_active=True,
        )
        user.set_password(password)
        user.save()

        token, created = TokenModel.objects.get_or_create(
            user=user
        )

        serializer = UserSerializer(user)
        return Response({
            'result': True,
            'massage': 'حساب کاربری با موفقیت ایجاد شد',
            'data': [{
                'token': token.key,
                'user-info': serializer.data,
            }]
        }, status=status.HTTP_201_CREATED)


class LoginUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginUserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'result': False,
                'message': 'اطلاعات وارد شده صحیح نیست.',
                'data': [
                    serializer.errors
                ]
            }, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        user = UserModel.objects.filter(email=email.lower()).first()

        if user is None:
            return Response({
                'result': False,
                'massage': 'کاربری با این ایمیل یافت نشد.',
                'data': []
            })

        if not user.check_password(password):
            return Response({
                'result': False,
                'massage': 'رمز عبور اشتباه است',
                'data': []
            }, status=status.HTTP_400_BAD_REQUEST)

        token, created = TokenModel.objects.get_or_create(user=user)

        serializer = UserSerializer(user)
        return Response({
            'result': True,
            'massage': 'ورود با موفقیت انجام شد',
            'data': [{
                'token': token.key,
                'user-info': serializer.data,
            }]
        }, status=status.HTTP_200_OK)


class SendVerifyCodeAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SendVerifyCodeSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'result': False,
                'message': 'اطلاعات وارد شده صحیح نیست.',
                'data': [
                    serializer.errors
                ]
            }, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data.get('email')

        user = UserModel.objects.filter(email=email.lower()).first()

        if user is None:
            return Response({
                'result': False,
                'massage': 'کاربری با این ایمیل یافت نشد.',
                'data': []
            }, status=status.HTTP_400_BAD_REQUEST)

        otp, created = OTPModel.objects.get_or_create(user=user)
        otp.otp = random_code(6)
        otp.save()

        try:
            send_mail(
                "Verify Code",
                f"It's your Code : {otp.otp}",
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            detail = 'کد تایید به ایمیل شما ارسال شد.'
        except Exception as e:
            detail = 'در ارسال کد مشکلی پیش آمده لطفا دوباره امتحان کنید.'

        return Response({
            'result': True,
            'massage': detail,
            'data': [
                {
                    'code': otp.otp,
                    'email': user.email,
                }
            ]
        }, status=status.HTTP_200_OK)


class ResetPasswordAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ResetPasswordSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'result': False,
                'message': 'اطلاعات وارد شده صحیح نیست.',
                'data': [
                    serializer.errors
                ]
            }, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        otp = serializer.validated_data.get('otp')

        user = UserModel.objects.filter(email=email.lower()).first()

        if user is None:
            return Response({
                'result': False,
                'massage': 'کاربری با این ایمیل یافت نشد.',
                'data': []
            }, status=status.HTTP_400_BAD_REQUEST)

        otp_object = OTPModel.objects.filter(user_id=user.id, otp=otp).first()

        if otp_object is None:
            return Response({
                'result': False,
                'massage': 'کد وارد شده اشتباه است',
                'data': []
            }, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(password)
        user.save()

        otp_object.delete()

        token, created = TokenModel.objects.get_or_create(user=user)
        serializer = UserSerializer(user)

        return Response({
            'result': True,
            'massage': 'رمز عبور با موفقیت تغییر کرد.',
            'data': [
                {
                    'token': token.key,
                    'user-info': serializer.data,
                }
            ]
        }, status=status.HTTP_200_OK)

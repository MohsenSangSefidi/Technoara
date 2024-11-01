from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView, Response
from rest_framework.generics import RetrieveAPIView
from rest_framework import status

from django.utils.crypto import get_random_string
from Utils.poll import verify_code
from .models import UserModel
from django.conf import settings
from django.core.mail import send_mail
from .serializers import (GetUserSerializer, ActiveUserSerializer, LoginUserSerializer, RegisterUserSerializer,
                          SendVerifyCodeSerializer)


class GetUserAPIView(RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = GetUserSerializer
    lookup_field = 'user_token'


class RegisterUserAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            avatar = serializer.validated_data.get('user_avatar')
            username = serializer.validated_data.get('username')
            first_name = serializer.validated_data.get('first_name')
            last_name = serializer.validated_data.get('last_name')
            password = serializer.validated_data.get('password')
            email = serializer.validated_data.get('email')
            check_user = UserModel.objects.filter(username=username, email=email.lower()).first()
            if check_user is None:
                user = UserModel(username=username, first_name=first_name, last_name=last_name, email=email.lower(),
                                 is_active=False, user_token=get_random_string(50), user_verify_code=verify_code(),
                                 user_avatar=avatar)
                user.set_password(password)
                user.save()

                HOST_EMAIL = settings.EMAIL_HOST_USER
                user_email = user.email
                detail = ''

                try:
                    send_mail(
                        "Verify Code",
                        f"It's your Code : {user.user_verify_code}",
                        HOST_EMAIL,
                        [user_email],
                        fail_silently=False,
                    )
                    detail = "Email Sent"
                except:
                    detail = 'Can\'t send email'

                serializer = GetUserSerializer(user)
                return Response({'detail': detail, 'user-detail': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({'detail': 'User Already Exists'}, status=status.HTTP_400_BAD_REQUEST)

        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActiveUserAPIView(APIView):

    def put(self, request, *args, **kwargs):
        serializer = ActiveUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_token = serializer.validated_data.get('user_token')
            verify_code = serializer.validated_data.get('verify_code')
            user = UserModel.objects.filter(user_token=user_token).first()
            if user is not None:
                if str(user.user_verify_code) == str(verify_code):
                    user.is_active = True
                    user.save()
                    return Response({'detail': 'User Activated'}, status=status.HTTP_200_OK)
                else:
                    return Response({'detail': 'Invalid Code'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'detail': 'User Not Found'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = UserModel.objects.filter(email=email.lower()).first()
            if user is not None:
                if user.check_password(password):
                    if user.is_active:
                        user.user_token = get_random_string(60)
                        user.save()
                        serializer = GetUserSerializer(user)
                        return Response({'token': user.user_token, 'user-detail': serializer.data},
                                        status=status.HTTP_200_OK)
                    else:
                        return Response({'detail': 'Account Disabale'}, status=status.HTTP_403_FORBIDDEN)
                else:
                    return Response({'detail': 'Invalid Password'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'detail': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SendVerifyCodeAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SendVerifyCodeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_token = serializer.validated_data.get('user_token')
            email = serializer.validated_data.get('email')

            user = UserModel.objects.filter(user_token=user_token, email=email.lower()).first()

            if user is not None:
                user.user_verify_code = verify_code()
                user_email = user.email
                user.save()

                HOST_EMAIL = settings.EMAIL_HOST_USER
                detail = ''

                try:
                    send_mail(
                        "Verify Code",
                        f"It's your Code : {user.user_verify_code}",
                        HOST_EMAIL,
                        [user_email.lower()],
                        fail_silently=False,
                    )
                    detail = "Email Sent"
                except Exception as e:
                    detail = 'Can\'t send email'

                return Response({'detail': detail}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'User Not Found'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

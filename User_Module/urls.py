from django.urls import path
from .views import GetUserAPIView, RegisterUserAPIView, ActiveUserAPIView, LoginUserAPIView, SendVerifyCodeAPIView

urlpatterns = [
    path('active-user/', ActiveUserAPIView.as_view()),
    path('create-user/', RegisterUserAPIView.as_view()),
    path('login-user/', LoginUserAPIView.as_view()),
    path('send-verify-code/', SendVerifyCodeAPIView.as_view()),
    path('get-user/<user_token>/', GetUserAPIView.as_view()),
]

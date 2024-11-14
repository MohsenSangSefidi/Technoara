from django.urls import path
from .views import GetUserAPIView, RegisterUserAPIView, LoginUserAPIView, SendVerifyCodeAPIView, ResetPasswordAPIView

urlpatterns = [
    path('create-user/', RegisterUserAPIView.as_view()),
    path('login-user/', LoginUserAPIView.as_view()),
    path('get-user/<email>/', GetUserAPIView.as_view()),
    path('send-verify-code/', SendVerifyCodeAPIView.as_view()),
    path('rest-password/', ResetPasswordAPIView.as_view())
]

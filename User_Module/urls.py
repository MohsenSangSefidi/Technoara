from django.urls import path
from .views import LoginUserView, RegisterUserView, GetUserView, SendVerifyCodeView, ResetPasswordView
urlpatterns = [
    path('create-user/', RegisterUserView.as_view()),
    path('login-user/', LoginUserView.as_view()),
    path('get-user/<email>/', GetUserView.as_view()),
    path('send-verify-code/', SendVerifyCodeView.as_view()),
    path('rest-password/', ResetPasswordView.as_view())
]

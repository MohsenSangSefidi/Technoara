from rest_framework.authentication import TokenAuthentication
from .models import TokenModel


class UserAuthentication(TokenAuthentication):
    model = TokenModel

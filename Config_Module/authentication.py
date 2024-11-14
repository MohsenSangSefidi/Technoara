from rest_framework.authentication import TokenAuthentication
from User_Module.models import TokenModel


class UserAuthentication(TokenAuthentication):
    model = TokenModel
    keyword = 'Technoara'

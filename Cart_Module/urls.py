from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('active-cart-info/', GetActiveCartInfoAPIView.as_view()),
    path('all-user-carts/', GetAllCartInfoAPIView.as_view()),
    path('update-cart-item/', UpdateCartItemAPIView.as_view()),
    path('delete-caet-item/', DeleteCartItemAPIView.as_view()),
    path('add-cart-item/', AddCartItemAPIView.as_view())
]

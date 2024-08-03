from django.urls import path
from .views import ProductApiView, ProductDetailApiView

urlpatterns = [
    path('all/', ProductApiView.as_view()),
    path('get/<int:pk>/', ProductDetailApiView.as_view()),
    path('post/<int:pk>/', ProductApiView.as_view())
]

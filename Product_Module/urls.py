from django.urls import path
from .views import ProductApiView, ProductDetailApiView, CraeteProductApiView

urlpatterns = [
    path('filter/', ProductApiView.as_view()),
    path('create/', CraeteProductApiView.as_view()),
    path('detail/<int:pk>/', ProductDetailApiView.as_view())
]

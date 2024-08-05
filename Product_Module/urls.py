from django.urls import path
from .views import ProductApiView, ProductDetailApiView

urlpatterns = [
    path('filter/', ProductApiView.as_view()),
    path('detail/<int:pk>/', ProductDetailApiView.as_view()),
    path('create/<int:pk>/', ProductApiView.as_view())
]

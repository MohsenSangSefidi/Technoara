from django.urls import path
from .views import ProductApiView, ProductDetailApiView, CreateProductApiView, CreateProductFeatureApiView, CreateProductImagesApiView

urlpatterns = [
    path('filter/', ProductApiView.as_view()),
    path('create/', CreateProductApiView.as_view()),
    path('create-feature/', CreateProductFeatureApiView.as_view()),
    path('create-images/', CreateProductImagesApiView.as_view()),
    path('detail/<int:pk>/', ProductDetailApiView.as_view())
]

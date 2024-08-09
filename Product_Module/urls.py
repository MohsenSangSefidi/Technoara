from django.urls import path
from .views import (ProductApiView, ProductDetailApiView, CreateProductApiView, CreateProductFeatureApiView,
                    CreateProductImagesApiView, CreateCommentApiView)

urlpatterns = [
    path('filter/', ProductApiView.as_view()),
    path('create-product/', CreateProductApiView.as_view()),
    path('create-comment/', CreateCommentApiView.as_view()),
    path('create-feature/', CreateProductFeatureApiView.as_view()),
    path('create-images/', CreateProductImagesApiView.as_view()),
    path('detail/<int:pk>/', ProductDetailApiView.as_view())
]

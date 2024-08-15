from django.urls import path
from .views import (FilterProductApiView, GetProductApiView, CreateProductApiView, CreateProductFeatureApiView,
                    CreateProductImagesApiView, CreateCommentApiView, GetCategoryApiView, GetProductCommentsApiView)

urlpatterns = [
    path('create-product/', CreateProductApiView.as_view()),
    path('create-comment/', CreateCommentApiView.as_view()),
    path('create-feature/', CreateProductFeatureApiView.as_view()),
    path('create-images/', CreateProductImagesApiView.as_view()),
    path('filter-product/', FilterProductApiView.as_view()),
    path('get-category/', GetCategoryApiView.as_view()),
    path('get-product-comments/<slug:slug>/', GetProductCommentsApiView.as_view()),
    path('get-product/<slug:slug>/', GetProductApiView.as_view())
]

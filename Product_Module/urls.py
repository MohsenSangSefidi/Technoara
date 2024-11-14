from django.urls import path, re_path
from .views import (FilterProductApiView, GetProductApiView, CreateProductApiView, CreateProductFeatureApiView,
                    CreateProductImagesApiView, CreateCommentApiView, GetCategoryApiView, GetProductCommentsApiView,
                    BannerApiView)

urlpatterns = [
    path('create-product/', CreateProductApiView.as_view()),
    path('create-comment/', CreateCommentApiView.as_view()),
    path('create-feature/', CreateProductFeatureApiView.as_view()),
    path('create-images/', CreateProductImagesApiView.as_view()),
    path('filter-product/', FilterProductApiView.as_view()),
    path('get-category/', GetCategoryApiView.as_view()),
    path('get-product-comments/', GetProductCommentsApiView.as_view()),
    path('get-product/', GetProductApiView.as_view()),
    path('banner/', BannerApiView.as_view()),
]

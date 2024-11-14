from django.urls import path
from .views import (
    FilterProductView, GetProductView, GetProductCommentsView, GetCategoryView, GetBannerView, CreateProductView,
    CreateProductFeatureView, CreateProductImagesView, CreateCommentView, CreateBannerView, CreateCategoryView,
    CreateSubCategoryView
)

urlpatterns = [
    path('filter-product/', FilterProductView.as_view(), name='filter-product'),
    path('get-product/', GetProductView.as_view(), name='get-product'),
    path('get-product-comment/', GetProductCommentsView.as_view(), name='get-product-comment'),
    path('get-category/', GetCategoryView.as_view(), name='get-category'),
    path('get-banner/', GetBannerView.as_view(), name='get-banner'),
    path('create-product/', CreateProductView.as_view(), name='create-product'),
    path('create-product-feature/', CreateProductFeatureView.as_view(), name='create-product-feature'),
    path('create-product-image/', CreateProductImagesView.as_view(), name='create-product-image'),
    path('create-comment/', CreateCommentView.as_view(), name='create-comment'),
    path('create-banner/', CreateBannerView.as_view(), name='create-banner'),
    path('create-category/', CreateCategoryView.as_view(), name='create-category'),
    path('create-sub-category/', CreateSubCategoryView.as_view(), name='create-sub-category'),
]

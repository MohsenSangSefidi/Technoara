from django.urls import path
from .views import BlogApiView, GetAllPostsApiView

urlpatterns = [
    path('blog-post/', BlogApiView.as_view()),
    path('blog-all-post/', GetAllPostsApiView.as_view())
]

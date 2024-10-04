from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.text import slugify
from rest_framework import status

from .authentication import TokenAuthentication
from .serializers import *
from .models import *


class BlogApiView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        info = InfoSerializer(data=request.data)
        if info.is_valid(raise_exception=True):
            post = Post.objects.filter(slug=info.validated_data.get('slug')).first()
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        info = CreatePostSerializer(data=request.data)
        if info.is_valid(raise_exception=True):
            title = info.validated_data.get('title')
            cover_img = info.validated_data.get('cover_img')
            user_token = info.validated_data.get('user_token')
            body = info.validated_data.get('body')
            user = UserModel.objects.filter(user_token=user_token).first()
            if user is not None:
                try:
                    post = Post(title=title, slug=slugify(title), cover_img=cover_img, author=user, body=body)
                    post.save()
                except Exception as e:
                    return Response({'detail': 'Title Exist'}, status=status.HTTP_400_BAD_REQUEST)
                serializer = PostSerializer(post)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"detail": "Author Doesn't Exist"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        info = UpdatePostSerializer(data=request.data)
        if info.is_valid(raise_exception=True):
            title = info.validated_data.get('title')
            cover_img = info.validated_data.get('cover_img')
            user_token = info.validated_data.get('user_token')
            body = info.validated_data.get('body')
            post_status = info.validated_data.get('status')
            slug = info.validated_data.get('slug')
            user = UserModel.objects.filter(user_token=user_token).first()
            if user is not None:
                post = Post.objects.filter(slug=slug).first()
                if post is not None:
                    if post_status == 'draft':
                        post.title = title
                        post.cover_img = cover_img
                        post.author = user
                        post.body = body
                        post.status = post_status
                        post.updated = timezone.now()
                        post.save()
                        serializer = PostSerializer(post)
                        return Response(serializer.data, status=status.HTTP_200_OK)
                    elif post_status == 'published':
                        post.title = title
                        post.cover_img = cover_img
                        post.author = user
                        post.body = body
                        post.status = post_status
                        post.updated = timezone.now()
                        post.publish = timezone.now()
                        post.save()
                        serializer = PostSerializer(post)
                        return Response(serializer.data, status=status.HTTP_200_OK)
                    else:
                        return Response({"detail": "Status must be ( draft ) or ( published )"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"detail": "Post Doesn't Exist"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"detail": "Author Doesn't Exist"}, status=status.HTTP_400_BAD_REQUEST)


class GetAllPostsApiView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(status='published').order_by('-updated')
        paginator = PageNumberPagination()
        paginator.page_size = 5
        result = paginator.paginate_queryset(post, request)
        serializer = PostSerializer(result, many=True)
        return paginator.get_paginated_response(serializer.data)

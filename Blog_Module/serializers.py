from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'cover_img_url',
            'slug',
            'author',
            'body',
            'publish',
            'created',
            'updated',
            'status'
        ]

    def get_author(self, obj):
        return {
            'username': obj.author.username,
            'email': obj.author.email,
        }


class InfoSerializer(serializers.Serializer):
    slug = serializers.CharField()

    class Meta:
        fields = ['slug']


class CreatePostSerializer(serializers.Serializer):
    title = serializers.CharField()
    cover_img = serializers.ImageField()
    user_token = serializers.CharField()
    body = serializers.CharField()

    class Meta:
        model = Post
        fields = [
            'title',
            'cover_img',
            'user_token',
            'body',
        ]


class UpdatePostSerializer(serializers.Serializer):
    title = serializers.CharField()
    cover_img = serializers.ImageField()
    user_token = serializers.CharField()
    body = serializers.CharField()
    status = serializers.CharField()
    slug = serializers.CharField()

    class Meta:
        fields = [
            'title',
            'cover_img',
            'user_token',
            'body',
            'status',
            'slug'
        ]

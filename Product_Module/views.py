from rest_framework.views import Response
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

from django.utils.text import slugify

from .authentication import TokenAuthentication
from .serializers import ProductListSerializer, ProductSerializer
from .models import ProductModel


class ProductApiView(CreateAPIView, ListModelMixin, GenericAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = ProductModel.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = LimitOffsetPagination

    def get(self, request, *args, **kwargs):

        return self.list(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        title = serializer.validated_data.get('product_title')
        slug = serializer.validated_data.get('product_slug') or None

        if slug is None:
            slug = slugify(title)

        serializer.save(slug=slug)


class ProductDetailApiView(RetrieveAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

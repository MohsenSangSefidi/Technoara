from rest_framework.views import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

from django.utils.text import slugify

from .authentication import TokenAuthentication
from .serializers import ProductListSerializer, ProductSerializer, ProductFilterSerializer
from .models import ProductModel, SubCategoryModel


class ProductApiView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        filter = ProductFilterSerializer(data=request.data)
        if filter.is_valid(raise_exception=True):

            # Serializer Data
            title = filter.validated_data.get('product_title')
            category = filter.validated_data.get('category_filter')
            price_start = filter.validated_data.get('price_filter_start')
            price_end = filter.validated_data.get('price_filter_end')

            if category or price_start or price_end:
                category_obj = SubCategoryModel.objects.filter(sub_category_slug=category if category else '').first()
                data = ProductModel.objects.filter(product_category_id=category_obj.id if category_obj else 0)
                if data:
                    data = data.filter(product_price__gte=price_start if price_start else 0,
                                       product_price__lte=price_end if price_end else 99999999,
                                       product_title__icontains=title if title else '')
                else:
                    data = ProductModel.objects.filter(product_price__gte=price_start if price_start else 0,
                                                       product_price__lte=price_end if price_end else 99999999,
                                                       product_title__icontains=title if title else '')

                serializer = ProductListSerializer(data, many=True).data
                return Response(serializer)

            else:
                data = ProductModel.objects.filter(product_is_active=True)
                serializer = ProductListSerializer(data, many=True).data
                return Response(serializer)

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

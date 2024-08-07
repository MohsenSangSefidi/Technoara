from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status

from django.utils.text import slugify

from .authentication import TokenAuthentication
from .serializers import (ProductListSerializer, ProductSerializer, ProductFilterSerializer, ProductCreateSerializer,
                          ProductFeatureSerializer, ProductImagesSerializer)
from .models import ProductModel, SubCategoryModel, ProductFeatureModel, ProductImagesModel


class ProductApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        filter = ProductFilterSerializer(data=request.data)
        if filter.is_valid(raise_exception=True):

            # Serializer Data
            title = filter.validated_data.get('product_title')
            category = filter.validated_data.get('category_filter')
            price_start = filter.validated_data.get('price_filter_start')
            price_end = filter.validated_data.get('price_filter_end')


            if title or category or price_start or price_end:
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
                serializer = ProductListSerializer(data,  many=True).data
                return Response(serializer)





class CreateProductApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        product = ProductCreateSerializer(data=request.data)

        if product.is_valid(raise_exception=True):
            title = product.validated_data.get('product_title')
            slug = slugify(title)

            check_product = ProductModel.objects.filter(product_slug=slug).first()

            if check_product is None:
                product.save(product_slug=slug)
                product = ProductModel.objects.filter(product_slug=slug).first()
            else:
                return Response({'detail' : 'Product already exists'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ProductSerializer(product).data

        return Response(serializer, status=status.HTTP_201_CREATED)


class CreateProductFeatureApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = ProductFeatureSerializer(data=request.data)
        if data.is_valid(raise_exception=True):
            product_id = data.validated_data.get('feature_product')
            feature_title = data.validated_data.get('feature_title')
            product = ProductModel.objects.filter(id=product_id.id).first()
            feature = product.productfeaturemodel_set.filter(feature_title=feature_title).first()
            if feature is None:
                data.save()
                return Response(data.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'detail' : 'Feature already exists'}, status=status.HTTP_400_BAD_REQUEST)


class CreateProductImagesApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        data = ProductImagesSerializer(data=request.data)
        if data.is_valid(raise_exception=True):
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'detail' : 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailApiView(RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

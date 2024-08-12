from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from django.utils.text import slugify

from .authentication import TokenAuthentication
from .serializers import *
from .models import ProductModel, SubCategoryModel, ProductFeatureModel, ProductImagesModel


class FilterProductApiView(APIView):
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

                paginator = PageNumberPagination()
                paginator.page_size = 2
                results_page = paginator.paginate_queryset(data, request)
                serializer = ProductListSerializer(results_page, many=True)
                return paginator.get_paginated_response(serializer.data)

            else:
                data = ProductModel.objects.filter(product_is_active=True)
                paginator = PageNumberPagination()
                paginator.page_size = 2
                results_page = paginator.paginate_queryset(data, request)
                serializer = ProductListSerializer(results_page, many=True)
                return paginator.get_paginated_response(serializer.data)

        else:
            return Response(filter.errors, status=status.HTTP_400_BAD_REQUEST)


class GetProductApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, slug, *args, **kwargs):
        product = ProductModel.objects.filter(product_slug=slug).first()
        if product is not None:
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Product does not exist'}, status=status.HTTP_400_BAD_REQUEST)


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
                serializer = ProductSerializer(product).data
                return Response(serializer, status=status.HTTP_201_CREATED)
            else:
                return Response({'detail': 'Product already exists'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateProductFeatureApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CreateProductFeatureSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            product_id = serializer.validated_data.get('feature_product')
            feature_title = serializer.validated_data.get('feature_title')
            product = ProductModel.objects.filter(id=product_id.id).first()
            feature = product.productfeaturemodel_set.filter(feature_title=feature_title).first()
            if feature is None:
                serializer.save()
                feature = ProductFeatureModel.objects.filter(feature_product=product_id, feature_title=feature_title).first()
                serializer = ProductFeatureSerializer(feature)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            else:
                return Response({'detail': 'Product does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateProductImagesApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = CreateProductImageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            img_id = serializer.data['id']
            img = ProductImagesModel.objects.filter(id=img_id).first()
            serializer = ProductImagesSerializer(img)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateCommentApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CreateProductCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            comment_rating = serializer.validated_data.get('comment_rating')
            if comment_rating <= 5:
                serializer.save()
                comment_id = serializer.data['id']
                print(comment_id)
                comment = ProductCommentModel.objects.filter(id=comment_id).first()
                serializer = ProductCommentSerializer(comment)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'detail': 'The rating is more than 5'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetCategoryApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        categories = CategoryModel.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

from django.http import HttpRequest
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from django.utils.text import slugify
from django.utils.encoding import uri_to_iri
from User_Module.authentication import UserAuthentication

from .authentication import TokenAuthentication
from .serializers import *
from .models import ProductModel, SubCategoryModel, ProductFeatureModel, ProductImagesModel, HomePageBannerModel


class FilterProductApiView(APIView):
    def get(self, request, *args, **kwargs):
        data = ProductFilterSerializer(data=request.data)
        if data.is_valid(raise_exception=True):

            # Serializer Data
            title = data.validated_data.get('product_title')
            category = data.validated_data.get('category_filter')
            price_start = data.validated_data.get('price_filter_start')
            price_end = data.validated_data.get('price_filter_end')

            filters = {}
            if title is not None:
                filters['title__icontains'] = title

            if category is not None:
                filters['product_category_id'] = category

            if price_start is not None:
                filters['product_price__gt'] = price_start

            if price_end is not None:
                filters['product_price__lt'] = price_end

            products = ProductModel.objects.filter(**filters)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class GetProductApiView(APIView):
    def get(self, request, *args, **kwargs):
        slug = request.query_params.get('slug')

        product = ProductModel.objects.filter(product_slug=slug).first()
        if product is not None:
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Product does not exist'}, status=status.HTTP_400_BAD_REQUEST)


class CreateProductApiView(APIView):
    authentication_classes = [UserAuthentication]
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


class GetProductCommentsApiView(APIView):
    def get(self, request, *args, **kwargs):
        slug = request.query_params.get('slug')

        product = ProductModel.objects.filter(product_slug=slug).first()
        comments = ProductCommentModel.objects.filter(comment_product=product)
        serializer = ProductCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateProductFeatureApiView(APIView):
    authentication_classes = [UserAuthentication]
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
    authentication_classes = [UserAuthentication]
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
    authentication_classes = [UserAuthentication]
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
    def get(self, request, *args, **kwargs):
        categories = CategoryModel.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BannerApiView(APIView):
    def get(self, request, *args, **kwargs):
        banner = HomePageBannerModel.objects.filter(is_active=True)
        serializer = BannerSerializer(banner, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = CraeteBannerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            name = serializer.validated_data.get('name')
            img = serializer.validated_data.get('img')
            url = serializer.validated_data.get('url')
            banner = HomePageBannerModel.objects.create(name=name, img=img, url=url)
            banner.save()
            serializer = BannerSerializer(banner)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# class CreateCategory(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = CreateCategorySerializer(data=request.data)

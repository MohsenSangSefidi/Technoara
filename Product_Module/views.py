from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework import status

from Config_Module.authentication import UserAuthentication
from django.utils.text import slugify
from django.db import IntegrityError

from .models import (
    ProductModel, ProductFeatureModel, ProductImagesModel, HomePageBannerModel, CategoryModel, ProductCommentModel,
    SubCategoryModel
)
from .serializers import (
    CreateProductFeatureSerializer, ProductImagesSerializer, CreateProductImageSerializer, ProductCommentSerializer,
    CreateProductCommentSerializer, CategorySerializer, BannerSerializer, CreateBannerSerializer,
    ProductListSerializer, ProductSerializer, ProductFilterSerializer, ProductFeatureSerializer,
    CreateCategorySerializer, ProductCreateSerializer, CreateSubCategorySerializer
)


class FilterProductView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = ProductFilterSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'result': False,
                'message': 'اطلاعات وارد شده صحیح نیست.',
                'data': [
                    serializer.errors
                ]
            }, status=status.HTTP_400_BAD_REQUEST)

        # Serializer Data
        title = serializer.validated_data.get('product_title')
        category = serializer.validated_data.get('category_filter')
        price_start = serializer.validated_data.get('price_filter_start')
        price_end = serializer.validated_data.get('price_filter_end')

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

        return Response({
            'result': True,
            'massage': f'تعداد {products.count()} یافت شد.',
            'data': [
                serializer.data
            ]
        }, status=status.HTTP_200_OK)


class GetProductView(APIView):
    def get(self, request, *args, **kwargs):
        slug = request.query_params.get('slug')

        product = ProductModel.objects.filter(product_slug=slug).first()

        if product is None:
            return Response({
                'result': False,
                'massage': 'محصولی یافت نشد.',
                'data': []
            })

        serializer = ProductSerializer(product)
        return Response({
            'result': True,
            'massage': 'محصول پیدا شد.',
            'data': [
                serializer.data
            ]
        }, status=status.HTTP_200_OK)


class GetProductCommentsView(APIView):
    def get(self, request, *args, **kwargs):
        slug = request.query_params.get('slug')

        product = ProductModel.objects.filter(product_slug=slug).first()

        if product is None:
            return Response({
                'result': False,
                'massage': 'محصولی یافت نشد.',
                'data': []
            })

        comments = ProductCommentModel.objects.filter(comment_product=product)
        serializer = ProductCommentSerializer(comments, many=True)

        return Response({
            'result': True,
            'massage': f'{comments.count()}پیدا شد.',
            'data': [
                serializer.data
            ]
        }, status=status.HTTP_200_OK)


class GetCategoryView(APIView):
    def get(self, request, *args, **kwargs):
        categories = CategoryModel.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response({
            'result': True,
            'massage': f'{categories.count()} دسته بندی پیدا شد.'
        }, status=status.HTTP_200_OK)


class GetBannerView(APIView):
    def get(self, request, *args, **kwargs):
        banner = HomePageBannerModel.objects.filter(is_active=True)
        serializer = BannerSerializer(banner, many=True)

        return Response({
            'result': True,
            'massage': f'{banner.count()} بنر پیدا شد.',
            'data': [
                serializer.data
            ]
        }, status=status.HTTP_200_OK)


class CreateProductView(APIView):
    authentication_classes = [UserAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = ProductCreateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'result': False,
                'message': 'اطلاعات وارد شده صحیح نیست.',
                'data': [
                    serializer.errors
                ]
            }, status=status.HTTP_400_BAD_REQUEST)

        title = serializer.validated_data.get('product_title')
        slug = slugify(title)

        check_product = ProductModel.objects.filter(product_slug=slug).first()

        if check_product is not None:
            return Response({
                'result': False,
                'massage': 'محصول با این عنوان از قبل موجود است.',
                'data': []
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(product_slug=slug)

        product = ProductModel.objects.filter(product_slug=slug).first()
        serializer = ProductSerializer(product)

        return Response({
            'result': True,
            'massage': 'محصول مورد نظر ایجاد شد.',
            'data': [
                serializer.data
            ]
        }, status=status.HTTP_201_CREATED)


class CreateProductFeatureView(APIView):
    authentication_classes = [UserAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CreateProductFeatureSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'result': False,
                'message': 'اطلاعات وارد شده صحیح نیست.',
                'data': [
                    serializer.errors
                ]
            }, status=status.HTTP_400_BAD_REQUEST)

        product_id = serializer.validated_data.get('feature_product')
        feature_title = serializer.validated_data.get('feature_title')

        product = ProductModel.objects.filter(id=product_id.id).first()

        if product is None:
            return Response({
                'result': False,
                'massage': 'محصولی یافت نشد.',
                'data': []
            })

        feature = product.productfeaturemodel_set.filter(feature_title=feature_title).first()

        if feature is not None:
            return Response({
                'result': False,
                'massage': 'ویژگی محصول از قبل موجود است.'
            })

        serializer.save()

        feature = ProductFeatureModel.objects.filter(feature_product=product_id, feature_title=feature_title).first()
        serializer = ProductFeatureSerializer(feature)

        return Response({
            'result': True,
            'massage': 'ویژگی مورد نظر ایجاد شد.',
            'data': [
                serializer.data
            ]
        }, status=status.HTTP_201_CREATED)


class CreateProductImagesView(APIView):
    authentication_classes = [UserAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = CreateProductImageSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'result': False,
                'message': 'اطلاعات وارد شده صحیح نیست.',
                'data': [
                    serializer.errors
                ]
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        img_id = serializer.data['id']
        img = ProductImagesModel.objects.filter(id=img_id).first()

        serializer = ProductImagesSerializer(img)
        return Response({
            'result': True,
            'massage': 'عکس محصول ایجاد شد.',
            'data': [
                serializer.data
            ]
        }, status=status.HTTP_201_CREATED)


class CreateCommentView(APIView):
    authentication_classes = [UserAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CreateProductCommentSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'result': False,
                'message': 'اطلاعات وارد شده صحیح نیست.',
                'data': [
                    serializer.errors
                ]
            }, status=status.HTTP_400_BAD_REQUEST)

        comment_rating = serializer.validated_data.get('comment_rating')

        if comment_rating >= 5:
            return Response({
                'result': False,
                'massage': 'امتیاز وارد شده بیشتر از 5 است.',
                'data': []
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        comment_id = serializer.data['id']
        comment = ProductCommentModel.objects.filter(id=comment_id).first()

        serializer = ProductCommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateBannerView(APIView):
    authentication_classes = [UserAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CreateBannerSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'result': False,
                'message': 'اطلاعات وارد شده صحیح نیست.',
                'data': [
                    serializer.errors
                ]
            }, status=status.HTTP_400_BAD_REQUEST)

        name = serializer.validated_data.get('name')
        img = serializer.validated_data.get('img')
        url = serializer.validated_data.get('url')

        try:
            banner = HomePageBannerModel.objects.create(name=name, img=img, url=url)
            banner.save()
            serializer = BannerSerializer(banner)
            return Response({
                'result': True,
                'massage': 'بنر با موفقیت ایجاد شد.'
            }, status=status.HTTP_201_CREATED)

        except IntegrityError as e:
            return Response({
                'result': False,
                'massage': 'مشکلی در ذخیره اطلاعات پیش آمده',
                'data': [
                    {
                        'error': e
                    }
                ]
            })


class CreateCategoryView(APIView):
    authentication_classes = [UserAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CreateCategorySerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'result': False,
                'message': 'اطلاعات وارد شده صحیح نیست.',
                'data': [
                    serializer.errors
                ]
            }, status=status.HTTP_400_BAD_REQUEST)

        title = serializer.validated_data.get('category_title')
        slug = slugify(title)

        category = CategoryModel.objects.filter(category_slug=slug).first()

        if category is not None:
            return Response({
                'result': False,
                'massage': 'این دسته بندی از قبل وجود دارد',
                'data': []
            }, status=status.HTTP_400_BAD_REQUEST)

        category = CategoryModel.objects.create(category_title=title, category_slug=slug)
        serializer = CategorySerializer(category)

        return Response({
            'result': True,
            'massage': 'دسته بندی مورد نظر ایجاد شد',
            'data': [
                serializer.data
            ]
        }, status=status.HTTP_201_CREATED)


class CreateSubCategoryView(APIView):
    authentication_classes = [UserAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CreateSubCategorySerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'result': False,
                'message': 'اطلاعات وارد شده صحیح نیست.',
                'data': [
                    serializer.errors
                ]
            }, status=status.HTTP_400_BAD_REQUEST)

        sub_category_title = serializer.validated_data.get('category_title')
        sub_category_slug = slugify(sub_category_title)
        category_slug = serializer.validated_data.get('category_slug')

        category = CategoryModel.objects.filter(category_slug=category_slug).first()

        if category is None:
            return Response({
                'result': False,
                'massage': 'این دسته بندی وجود ندارد.',
                'data': []
            }, status=status.HTTP_400_BAD_REQUEST)

        sub_category = SubCategoryModel.objects.filter(category_slug=category_slug).first()

        if sub_category is not None:
            return Response({
                'result': False,
                'massage': 'این زیر دسته بندی از قبل موجود است.',
                'data': []
            }, status=status.HTTP_400_BAD_REQUEST)

        sub_category = SubCategoryModel.objects.create(
            sub_category_title=sub_category_title, sub_category_slug=sub_category_slug, sub_category_parent=category
        )

        serializer = CategorySerializer(category)
        return Response({
            'result': True,
            'massage': 'زیر دسته بندی مورد نظر ایجاد شد.',
            'data': [
                serializer.data
            ]
        }, status=status.HTTP_201_CREATED)

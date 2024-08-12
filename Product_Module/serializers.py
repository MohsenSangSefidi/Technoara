from rest_framework import serializers
from .models import ProductModel, ProductFeatureModel, ProductImagesModel, ProductCommentModel, CategoryModel


class ProductListSerializer(serializers.ModelSerializer):
    product_sub_category = serializers.SerializerMethodField(read_only=True)
    product_category = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ProductModel
        fields = [
            'id',
            'product_title',
            'product_description',
            'product_price',
            'product_sale_count',
            'product_create_date',
            'product_slug',
            'product_sub_category',
            'product_category',
            'product_discount',
            'product_discount_price',
            'product_discount_date',
            'product_cover_url'
        ]

    def get_product_sub_category(self, obj: ProductModel):
        return {
            'sub_category_id': obj.product_category.id,
            'sub_category_title': obj.product_category.sub_category_title,
            'sub_category_slug': obj.product_category.sub_category_slug
        }

    def get_product_category(self, obj: ProductModel):
        return {
            'category_id': obj.product_category.sub_category_parent.id,
            'category_title': obj.product_category.sub_category_parent.category_title,
            'category_slug': obj.product_category.sub_category_parent.category_slug
        }


class ProductSerializer(serializers.ModelSerializer):
    product_sub_category = serializers.SerializerMethodField(read_only=True)
    product_category = serializers.SerializerMethodField(read_only=True)
    product_images = serializers.SerializerMethodField(read_only=True)
    product_feature = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ProductModel
        fields = [
            'id',
            'product_title',
            'product_description',
            'product_price',
            'product_sale_count',
            'product_create_date',
            'product_slug',
            'product_discount',
            'product_discount_price',
            'product_discount_date',
            'product_comment_count',
            'product_rating',
            'product_cover_url',
            'product_sub_category',
            'product_category',
            'product_images',
            'product_feature'
        ]

    def get_product_sub_category(self, obj: ProductModel):
        return {
            'sub_category_id': obj.product_category.id,
            'sub_category_title': obj.product_category.sub_category_title,
            'sub_category_slug': obj.product_category.sub_category_slug
        }

    def get_product_category(self, obj: ProductModel):
        return {
            'category_id': obj.product_category.sub_category_parent.id,
            'category_title': obj.product_category.sub_category_parent.category_title,
            'category_slug': obj.product_category.sub_category_parent.category_slug
        }

    def get_product_images(self, obj: ProductModel):
        query = obj.productimagesmodel_set.all()
        data = []
        if query is not None:
            for item in query:
                image = {
                    'product_image_id': item.id,
                    'product_image_url': item.product_img_url()
                }
                data.append(image)

        return data

    def get_product_feature(self, obj: ProductModel):
        query = obj.productfeaturemodel_set.all()
        data = []
        if query is not None:
            for item in query:
                feature = {
                    'feature_title': item.feature_title,
                    'featuer_description': item.feature_description
                }
                data.append(feature)

        return data


class ProductFilterSerializer(serializers.Serializer):
    product_title = serializers.CharField(required=False)
    category_filter = serializers.CharField(required=False)
    price_filter_start = serializers.IntegerField(required=False)
    price_filter_end = serializers.IntegerField(required=False)

    class Meta:
        fields = [
            'product_title',
            'category_filter',
            'price_filter_start',
            'price_filter_end'
        ]


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = [
            'product_title',
            'product_description',
            'product_price',
            'product_category',
            'product_discount',
            'product_discount_date',
            'product_cover',
        ]


class ProductFeatureSerializer(serializers.ModelSerializer):
    feature_product = serializers.SerializerMethodField()

    class Meta:
        model = ProductFeatureModel
        fields = [
            'id',
            'feature_title',
            'feature_description',
            'feature_product'
        ]

    def get_feature_product(self, obj: ProductFeatureModel):
        return {
            'product_id': obj.feature_product.id,
            'product_title': obj.feature_product.product_title,
            'product_slug': obj.feature_product.product_slug
        }


class CreateProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeatureModel
        fields = [
            'id',
            'feature_title',
            'feature_description',
            'feature_product'
        ]


class ProductImagesSerializer(serializers.ModelSerializer):
    product_detail = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ProductImagesModel
        fields = [
            'id',
            'product_img_url',
            'product_detail'
        ]

    def get_product_detail(self, obj: ProductImagesModel):
        return {
            'product_id' : obj.product.id,
            'product_title': obj.product.product_title,
            'product_slug': obj.product.product_slug
        }

class CreateProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImagesModel
        fields = [
            'id',
            'product_img',
            'product'
        ]


class ProductCommentSerializer(serializers.ModelSerializer):
    comment_product = serializers.SerializerMethodField(read_only=True)
    comment_user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ProductCommentModel
        fields = [
            'id',
            'comment_text',
            'comment_rating',
            'comment_create_date',
            'comment_product',
            'comment_user'
        ]

    def get_comment_product(self, obj: ProductCommentModel):
        return {
            'product_id': obj.comment_product.id,
            'product_title': obj.comment_product.product_title,
            'product_slug': obj.comment_product.product_slug
        }

    def get_comment_user(self, obj: ProductCommentModel):
        return {
            'user_id': obj.comment_user.id,
            'user_name': obj.comment_user.username,
            'user_email': obj.comment_user.email
        }


class CreateProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCommentModel
        fields = [
            'id',
            'comment_text',
            'comment_rating',
            'comment_product',
            'comment_user'
        ]


class CategorySerializer(serializers.ModelSerializer):
    sub_categories = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CategoryModel
        fields = [
            'id',
            'category_title',
            'category_slug',
            'sub_categories'
        ]

    def get_sub_categories(self, obj: CategoryModel):
        list = []
        for item in obj.subcategorymodel_set.all():
            list.append({
                'sub_category_id': item.id,
                'sub_category_title': item.sub_category_title,
                'sub_category_slug': item.sub_category_slug
            })
        return list
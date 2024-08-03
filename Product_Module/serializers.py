from rest_framework import serializers
from .models import ProductModel


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
            'product_create_date',
            'product_slug',
            'product_sub_category',
            'product_category',
            'product_discount',
            'product_discount_date',
            'product_cover'
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
            'product_create_date',
            'product_slug',
            'product_discount',
            'product_discount_price',
            'product_discount_date',
            'product_comment_count',
            'product_rating',
            'product_cover',
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
                    'product_image_url': item.product_img.url
                }
                data.append(image)

        return data

    def get_product_feature(self, obj: ProductModel):
        query = obj.productfeaturemodel_set.all()
        data = []
        if query is not None:
            for item in query:
                feature = {
                    'feature_title' : item.feature_title,
                    'featuer_description' : item.feature_description
                }
                data.append(feature)

        return data

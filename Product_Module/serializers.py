from rest_framework import serializers
from .models import ProductModel


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = [
            'id',
            'product_title',
            'product_description',
            'product_price',
            'product_create_date',
            'product_slug',
            'product_category',
            'product_discount',
            'product_discount_date',
            'product_cover'
        ]

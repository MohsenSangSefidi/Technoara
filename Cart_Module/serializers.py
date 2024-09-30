from rest_framework import serializers
from .models import CartModel, CartItemModel


class CartSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    cart_items = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CartModel
        fields = [
            'detail',
            'is_paid',
            'paid_date',
            'created_at',
            'final_price',
            'user',
            'cart_items'
        ]

    def get_user(self, obj: CartModel):
        return {
            'id': obj.user.id,
            'username': obj.user.username,
            'email': obj.user.email,
            'token': obj.user.user_token,
        }

    def get_cart_items(self, obj: CartModel):
        list = []
        for item in obj.cartitemmodel_set.all():
            list.append({
                'id': item.id,
                'title': item.product.product_title,
                'cover': item.product.product_cover_url(),
                'price': item.product.product_price,
                'slug': item.product.product_slug,
                'discount': item.product.product_discount,
                'discount_price': item.product.product_discount_price(),
            })
        return list


class CartItemSerializer(serializers.ModelSerializer):
    cart = serializers.SerializerMethodField(read_only=True)
    product = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CartItemModel
        fields = [
            'cart',
            'product',
            'count'
        ]

    def get_cart(self, obj: CartItemModel):
        return {
            'id': obj.cart.id,
            'user': {
                'id': obj.cart.user.id,
                'username': obj.cart.user.username,
                'email': obj.cart.user.email,
            }
        }

    def get_product(self, obj: CartItemModel):
        return {
            'id': obj.product.id,
            'title': obj.product.product_title,
            'cover': obj.product.product_cover_url(),
            'price': obj.product.product_price,
            'slug': obj.product.product_slug,
            'discount': obj.product.product_discount,
            'discount_price': obj.product.product_discount_price(),
        }


class GetUserInfo(serializers.Serializer):
    user_token = serializers.CharField(max_length=150)

    class Meta:
        fields = ['user_token']


class GetCartItemSerializer(serializers.Serializer):
    user_token = serializers.CharField(max_length=150)
    product_slug = serializers.CharField(max_length=150)
    method = serializers.CharField(max_length=10)

    class Meta:
        fields = [
            'user_token',
            'product_slug',
            'method'
        ]


class DeleteCartItemSerializer(serializers.Serializer):
    user_token = serializers.CharField(max_length=150)
    product_slug = serializers.CharField(max_length=150)

    class Meta:
        fields = [
            'user_token',
            'product_slug'
        ]


class AddCartItemSerializer(serializers.Serializer):
    user_token = serializers.CharField(max_length=150)
    product_slug = serializers.CharField(max_length=150)
    count = serializers.IntegerField()

    class Meta:
        fields = [
            'user_token',
            'product_slug',
            'count'
        ]

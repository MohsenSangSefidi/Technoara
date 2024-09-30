from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from User_Module.models import UserModel

from .authentication import TokenAuthentication
from .serializers import *
from .models import *


class GetActiveCartInfoAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_info = GetUserInfo(data=request.data)
        if user_info.is_valid(raise_exception=True):
            user = UserModel.objects.filter(user_token=user_info.data['user_token']).first()
            if user is not None:
                cart, created = CartModel.objects.get_or_create(is_paid=False, user=user)
                serializer = CartSerializer(cart)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'User Not Found'}, status=status.HTTP_404_NOT_FOUND)


class GetAllCartInfoAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_info = GetUserInfo(data=request.data)
        if user_info.is_valid(raise_exception=True):
            user = UserModel.objects.filter(user_token=user_info.data['user_token']).first()
            if user is not None:
                carts = CartModel.objects.filter(user=user)
                serializer = CartSerializer(carts, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'User Not Found'}, status=status.HTTP_404_NOT_FOUND)


class UpdateCartItemAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        cart_item = GetCartItemSerializer(data=request.data)
        if cart_item.is_valid(raise_exception=True):
            user = UserModel.objects.filter(user_token=cart_item.data['user_token']).first()
            if user is not None:
                cart, created = CartModel.objects.get_or_create(user=user, is_paid=False)
                product = CartItemModel.objects.filter(cart=cart,
                                                       product__product_slug=cart_item.data['product_slug']).first()
                if product is not None:
                    if cart_item.data['method'] == 'Add':
                        product.count = product.count + 1
                        if product.count > product.product.product_count:
                            return Response({'detail': 'Product Count Limited'}, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            product.save()
                            serializer = CartItemSerializer(product)
                            return Response(serializer.data, status=status.HTTP_200_OK)
                    elif cart_item.data['method'] == 'Decrease':
                        product.count = product.count - 1
                        if product.count == 0:
                            return Response({'detail': 'Product Count Limited'}, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            product.save()
                            serializer = CartItemSerializer(product)
                            return Response(serializer.data, status=status.HTTP_200_OK)
                    else:
                        return Response({'detail': 'Method not allowed. It must be ( Add ) or ( Decrease )'},
                                        status=status.HTTP_405_METHOD_NOT_ALLOWED)
                else:
                    return Response({'detail': 'Cart Item Not Found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'detail': 'User Not Found'}, status=status.HTTP_404_NOT_FOUND)


class DeleteCartItemAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        cart_item = DeleteCartItemSerializer(data=request.data)
        if cart_item.is_valid(raise_exception=True):
            user = UserModel.objects.filter(user_token=cart_item.data['user_token']).first()
            if user is not None:
                cart, created = CartModel.objects.get_or_create(user=user, is_paid=False)
                product = CartItemModel.objects.filter(cart=cart, product__product_slug=cart_item.data['product_slug']).first()
                if product is not None:
                    product.delete()
                    return Response({'detail': 'Product Deleted'}, status=status.HTTP_200_OK)
                else:
                    return Response({'detail': 'Cart Item Not Found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'detail': 'User Not Found'}, status=status.HTTP_404_NOT_FOUND)


class AddCartItemAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        info = AddCartItemSerializer(data=request.data)
        if info.is_valid(raise_exception=True):
            user = UserModel.objects.filter(user_token=info.data['user_token']).first()
            if user is not None:
                cart, created = CartModel.objects.get_or_create(user=user, is_paid=False)
                product = ProductModel.objects.filter(product_slug=info.data['product_slug']).first()
                if product is not None:
                    cart_item, created = CartItemModel.objects.get_or_create(cart=cart, product=product)
                    cart_item.count = info.data['count']
                    cart_item.save()
                    serializer = CartItemSerializer(cart_item)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({'detail': 'Cart Item Not Found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'detail': 'User Not Found'}, status=status.HTTP_404_NOT_FOUND)


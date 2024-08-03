from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated

from .authentication import TokenAuthentication
from .serializers import ProductSerializer
from .models import ProductModel


class ProductApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = ProductModel.objects.all()
        query = ProductSerializer(data, many=True).data

        return Response(query)

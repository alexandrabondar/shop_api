from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import *


# ------- Shop View -------

class ShopReadApi(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated]


class ShopCreateApi(generics.CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated]


class ShopRetrieveUpdateDeleteApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated]


# ------- Storage View -------

class StorageReadApi(generics.ListAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    permission_classes = [IsAuthenticated]


class StorageCreateApi(generics.CreateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    permission_classes = [IsAuthenticated]


class StorageRetrieveUpdateDeleteApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    permission_classes = [IsAuthenticated]


# ------- Category View -------

class CategoryReadApi(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class CategoryCreateApi(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class CategoryRetrieveUpdateDeleteApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


# ------- Product View -------

class ProductReadApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductCreateApi(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductRetrieveUpdateDeleteApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


# ------- Sold Product View -------

class SoldProductReadApi(generics.ListAPIView):
    queryset = Product.objects.select_related('storage', 'storage__shop')
    serializer_class = SoldProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.query_params.get('product'):
            query = qs.filter(count_sold__gt=0, id=self.request.query_params.get('product'))
        elif self.request.query_params.get('shop'):
            query = qs.filter(count_sold__gt=0, shop=self.request.query_params.get('shop'))
        elif self.request.query_params.get('category'):
            query = qs.filter(count_sold__gt=0, category=self.request.query_params.get('category'))
        elif self.request.query_params.get('storage'):
            query = qs.filter(count_sold__gt=0, storage=self.request.query_params.get('storage'))
        else:
            query = qs.filter(count_sold__gt=0)
        return query


class ProductForSaleApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        queryset = Product.objects.get(id=pk)
        serializer_class = SoldProductSerializer(queryset)
        return Response(serializer_class.data)

    def post(self, request, pk):
        product = Product.objects.get(id=pk)
        serializer_class = ProductForSaleSerializer
        if request.data['count'] <= product.count:
            Product.objects.all().filter(id=pk).update(
                count=product.count-request.data['count'],
                count_sold=product.count_sold+request.data['count']
            )
            return Response(serializer_class(Product.objects.get(id=pk)).data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer_class.errors)


from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', queryset=Category.objects.all())
    storage = serializers.SlugRelatedField(slug_field='title', queryset=Storage.objects.all())
    shop = serializers.SlugRelatedField(slug_field='title', queryset=Shop.objects.all())

    class Meta:
        model = Product
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'


class SoldProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', queryset=Category.objects.all())
    storage = serializers.SlugRelatedField(slug_field='title', queryset=Storage.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'title', 'category', 'storage', 'count_sold']


class ProductForSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'count']

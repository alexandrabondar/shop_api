from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


USER_SHOP_API = get_user_model()


class UserProfile(models.Model):
    user = models.ForeignKey(
        USER_SHOP_API, verbose_name='Account', on_delete=models.CASCADE
    )


class Shop(models.Model):
    title = models.CharField("shop title", max_length=100, unique=True)

    class Meta:
        verbose_name = "Shop"
        verbose_name_plural = "Shops"


class Storage(models.Model):
    title = models.PositiveIntegerField("storage title", unique=True)
    shop = models.ForeignKey(
        Shop, verbose_name="Shop", on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name = "Storage"
        verbose_name_plural = "Storages"


class Category(models.Model):
    title = models.CharField("category title", max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    title = models.CharField("product title", max_length=100)
    category = models.ForeignKey(
        Category, verbose_name="Category", on_delete=models.CASCADE
    )
    count = models.PositiveIntegerField("count")
    storage = models.ForeignKey(
        Storage, verbose_name="Storage", on_delete=models.CASCADE
    )
    shop = models.ForeignKey(
        Shop, verbose_name="Shop", on_delete=models.CASCADE
    )
    count_sold = models.PositiveIntegerField("count sold", null=True, default=0)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

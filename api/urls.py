from django.urls import path, include

from .views import *

urlpatterns = [
    path('shops/', ShopReadApi.as_view()),
    path('shops/create/', ShopCreateApi.as_view()),
    path('shops/<int:pk>/', ShopRetrieveUpdateDeleteApi.as_view()),
    path('storages/', StorageReadApi.as_view()),
    path('storages/create/', StorageCreateApi.as_view()),
    path('storages/<int:pk>/', StorageRetrieveUpdateDeleteApi.as_view()),
    path('categories/', CategoryReadApi.as_view()),
    path('categories/create/', CategoryCreateApi.as_view()),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDeleteApi.as_view()),
    path('products/', ProductReadApi.as_view()),
    path('products/create/', ProductCreateApi.as_view()),
    path('products/<int:pk>/', ProductRetrieveUpdateDeleteApi.as_view()),
    path('products/<int:pk>/sell/', ProductForSaleApi.as_view()),
    path('sold-products/', SoldProductReadApi.as_view()),
    path('rest-auth/', include('rest_auth.urls'))
]

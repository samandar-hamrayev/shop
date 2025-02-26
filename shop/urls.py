from django.urls import path
from .views import index, product_detail, products_by_category

urlpatterns = [
    path('home/', index, name='index'),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),
    path('category/<int:id>/', products_by_category, name='category_products'),
]
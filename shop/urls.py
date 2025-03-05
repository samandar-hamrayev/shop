from django.urls import path
from .views import (
    index,
    product_detail,
    products_by_category,
    product_create,
    product_update,
    product_delete,
    create_order
)

urlpatterns = [
    path('home/', index, name='index'),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),
    path('product_detail/<int:id>/update', product_update, name='product_update'),
    path('product_detail/<int:id>/delete', product_delete, name='product_delete'),
    path('product/<int:id>/order/', create_order, name='create_order'),
    path('category/<int:id>/', products_by_category, name='category_products'),
    path('product-create/', product_create, name='product_create')
]
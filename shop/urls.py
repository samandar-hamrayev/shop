from django.urls import path
from .views import index, product_detail

urlpatterns = [
    path('home/', index, name='index'),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),
]
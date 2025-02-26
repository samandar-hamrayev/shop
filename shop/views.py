from django.shortcuts import render
from .models import Product
from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def index(request):
    products = Product.objects.all().order_by('-updated_at')
    categories = Category.objects.all().order_by('-updated_at')
    return render(request, 'shop/home.html',  context={'products': products, 'categories': categories})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shop/detail.html', {'product': product})


def products_by_category(request, id):
    category = get_object_or_404(Category, id=id)
    categories = Category.objects.all()
    products = Product.objects.filter(category=category)

    return render(request, 'shop/home.html', {'categories': categories, 'products': products, 'selected_category': category})
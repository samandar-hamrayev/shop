from django.shortcuts import render
from .models import Product
from django.shortcuts import render, get_object_or_404
from .models import Product


def index(request):
    products = Product.objects.all().order_by('-updated_at')
    context = {
        'products': products
    }
    return render(request, 'shop/home.html', context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shop/detail.html', {'product': product})

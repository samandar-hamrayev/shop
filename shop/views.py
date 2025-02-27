from idlelib.rpc import request_queue

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CommentForm,ProductCreateForm
from .models import Product
from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def index(request):
    products = Product.objects.all().order_by('-updated_at')
    categories = Category.objects.all().order_by('-updated_at')
    return render(request, 'shop/home.html',  context={'products': products, 'categories': categories})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    comments = product.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('product_detail', id=product.id)
    else:
        form = CommentForm()

    return render(request, 'shop/detail.html', {'product': product, 'comments': comments, 'form': form})


def products_by_category(request, id):
    category = get_object_or_404(Category, id=id)
    categories = Category.objects.all()
    products = Product.objects.filter(category=category)

    return render(request, 'shop/home.html', {'categories': categories, 'products': products, 'selected_category': category})



def product_create(request):
    form = ProductCreateForm()
    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'shop/add-product.html', context)


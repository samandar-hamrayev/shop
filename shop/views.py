from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .forms import CommentCreateForm, ProductCreateForm
from .models import Product, Category


def index(request):
    query = request.GET.get('q', '')
    products = Product.objects.all().order_by('-updated_at')
    if query:
        products = Product.objects.filter(name__icontains=query)
    categories = Category.objects.all().order_by('-updated_at')
    return render(request, 'shop/home.html',  context={'products': products, 'categories': categories})


def product_detail(request, id):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        categories = Category.objects.all().order_by('-updated_at')
        return render(request, 'shop/home.html', context={'products': products, 'categories': categories})
    product = Product.objects.filter(id=id).first()
    comments = product.comments.all()

    if request.method == "POST":
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('product_detail', id=product.id)
    else:
        form = CommentCreateForm()
    return render(request, 'shop/product_detail.html', {'product': product, 'comments': comments, 'form': form})


def products_by_category(request, id):
    category = Category.objects.filter(id = id).first()
    categories = Category.objects.all()
    products = Product.objects.filter(category=category)
    return render(request, 'shop/home.html', {'categories': categories, 'products': products, 'selected_category': category})


@user_passes_test(lambda user: user.is_superuser)
def product_create(request):
    form = ProductCreateForm()
    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'shop/product_create.html', context = {'form': form})


@user_passes_test(lambda user: user.is_superuser)
def product_update(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', id = product.id)
    else:
        form = ProductCreateForm(instance=product)
    return render(request, template_name='shop/product_update.html', context={'form': form, 'product': product})


@user_passes_test(lambda user: user.is_superuser)
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('index')
    return redirect('product_detail', id)





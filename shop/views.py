from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .forms import CommentCreateForm, ProductCreateForm, OrderCreateForm
from .models import Product, Category


def index(request):
    query = request.GET.get('q', '')
    products = Product.objects.all().order_by('-updated_at')
    if query:
        products = Product.objects.filter(name__icontains=query)
    categories = Category.objects.all().order_by('-updated_at')

    filter_query = request.GET.get('filter')
    if filter_query == "expensive":
        products = products.order_by('-price')
    elif filter_query == "cheap":
        products = products.order_by('price')

    return render(request, 'shop/home.html',  context={'products': products, 'categories': categories})


def product_detail(request, id):
    global comment_form

    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        categories = Category.objects.all().order_by('-updated_at')
        return render(request, 'shop/home.html', context={'products': products, 'categories': categories})

    product = Product.objects.filter(id=id).first()
    if not product:
        return redirect('index')

    comments = product.comments.all()

    if request.method == "POST" and 'comment_submit' in request.POST:
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('product_detail', id=product.id)
    else:
        comment_form = CommentCreateForm()

    order_form = OrderCreateForm()

    related_products = Product.objects.filter(category=product.category).exclude(id=product.id).order_by('-created_at')[
                       :4]

    return render(request, 'shop/product_detail.html', {
        'product': product,
        'comments': comments,
        'comment_form': comment_form,
        'order_form': order_form,
        'related_products': related_products,
    })


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


def create_order(request, id):
    product = get_object_or_404(Product, id=id)
    order_form = OrderCreateForm(request.POST or None)

    if request.method == 'POST' and order_form.is_valid():
        order_data = order_form.cleaned_data
        order_quantity = order_data['quantity']

        if 'confirm_order' in request.POST:
            order = order_form.save(commit=False)
            order.product = product

            if order_quantity > product.quantity:
                messages.error(request, f"Sorry, only {product.quantity} items are available!")
            else:
                order.save()
                product.quantity -= order_quantity
                product.save()
                messages.success(request, f"{order_quantity} {product.name} successfully ordered!")
            return redirect('product_detail', id=product.id)

        return render(request, 'shop/product_detail.html', {
            'product': product,
            'comments': product.comments.all(),
            'order_form': order_form,
            'comment_form': CommentCreateForm(),
            'order_data': order_data,
            'show_confirmation': True,
        })

    return render(request, 'shop/product_detail.html', {
        'product': product,
        'comments': product.comments.all(),
        'order_form': order_form,
        'comment_form': CommentCreateForm(),
    })




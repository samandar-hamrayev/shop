from django import forms
from django.core.validators import MaxValueValidator

from .models import Comment, Product, Order
from django import forms
from .models import Comment, Product

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write your comment'}),
        }


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'discount', 'category', 'rating', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the price'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Discount (%)'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'rating': forms.Select(attrs={'class': 'form-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
        }

class OrderCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'initial' in kwargs and 'product' in kwargs['initial']:
            product = kwargs['initial']['product']
            self.fields['quantity'].widget.attrs['max'] = min(product.quantity, 4)

    class Meta:
        model = Order
        fields = ['name', 'phone', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingiz'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+998901234567'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }
from django import forms
from .models import Comment, Product

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

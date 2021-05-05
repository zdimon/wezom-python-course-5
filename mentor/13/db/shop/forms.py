from django.forms import ModelForm
from shop.models import Category, Product

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category']
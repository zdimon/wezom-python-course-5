from django.shortcuts import render
from shop.models import Category, Product


def shop_list(request,cat_id=0):
    categories = Category.objects.all()
    if cat_id == 0:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category_id=cat_id)
    return render(request, 'shoplist.html', {
        "categories": categories,
        "products": products
    })
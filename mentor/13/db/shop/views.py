from django.shortcuts import render
from shop.models import Category


def shop_list(request):
    categories = Category.objects.all()
    return render(request, 'shoplist.html', {
        "categories": categories
    })
from django.shortcuts import render
from shop.models import Category, Product
from shop.forms import CategoryForm

def shop_list(request,cat_id=0):

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            o = form.save()
    categories = Category.objects.all()
    form = CategoryForm()
    if cat_id == 0:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category_id=cat_id)
    return render(request, 'shoplist.html', {
        "categories": categories,
        "products": products,
        "form": form
    })
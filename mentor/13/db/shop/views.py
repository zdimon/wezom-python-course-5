from django.shortcuts import render
from shop.models import Category, Product
from shop.forms import CategoryForm, ProductForm
from django.shortcuts import redirect


def save_product(request,cat_id=0):
    if request.method == "POST":
        form_product = ProductForm(request.POST)
        if form_product.is_valid():
            p = form_product.save()
        return redirect('/shop')

def shop_list(request,cat_id=0):

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            o = form.save()

    categories = Category.objects.all()
    form = CategoryForm()
    form_product = ProductForm()
    if cat_id == 0:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category_id=cat_id)
    return render(request, 'shoplist.html', {
        "categories": categories,
        "products": products,
        "form": form,
        "form_product": form_product
    })
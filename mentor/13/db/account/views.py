from django.shortcuts import render
from .forms import AccountForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from shop.models import Product2User
from django.contrib.auth import logout

def exit(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Goodbye!')
    return redirect('/shop')


def cart(request):
    items = Product2User.objects.filter(user=request.user.account)
    return render(request, 'cart.html', {
        "items": items
    })


def register(request):

    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.is_staff = True
            user.is_superuser = True
            user.set_password(request.POST["password"])
            user.save()
            login(request, user)
            messages.add_message(request, messages.INFO, 'Welcome!!!!.')
            return redirect('/shop')


    form = AccountForm()
    return render(request, 'register.html', {
        "form": form
    })

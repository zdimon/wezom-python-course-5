from django.shortcuts import render
from main.models import Page

def main(request):
    #page = Page.objects.filter(alias='main')
    page = Page.objects.get(alias='main')
    return render(request,'index.html', {"page": page})

def page(request, page_name):
    page = Page.objects.get(alias=page_name)
    return render(request,'index.html', {"page": page})

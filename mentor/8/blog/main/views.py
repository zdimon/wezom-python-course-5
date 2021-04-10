from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html',{"name": "Dima"})
    #return HttpResponse('<h1>Hello</h1>')

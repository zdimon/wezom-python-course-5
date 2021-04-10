# Создаем приложение 

    ./manage.py startapp shop

## Определяем функцию-контроллер shop/views.py

    from django.shortcuts import render
    from django.http import HttpResponse

    def index(request):
        return render(request,'index.html')

## Присоединяем функцию к url адресу shop/shop/urls.py


    from shop.views import index

    urlpatterns = [
        path('', index),
        path('admin/', admin.site.urls),
    ]
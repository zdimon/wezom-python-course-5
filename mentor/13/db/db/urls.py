
from django.contrib import admin
from django.urls import path
from main.views import main, page


urlpatterns = [
    path('', main),
    path('<slug:page_name>', page),
    path('admin/', admin.site.urls),
]

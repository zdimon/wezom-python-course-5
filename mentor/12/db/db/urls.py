
from django.contrib import admin
from django.urls import path
from main.views import main


urlpatterns = [
    path('', main),
    path('admin/', admin.site.urls),
]

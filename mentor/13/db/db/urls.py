
from django.contrib import admin
from django.urls import path
from main.views import main, page


urlpatterns = [
    path('', main),
    path('<slug:page_name>', page),
    path('admin/', admin.site.urls),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

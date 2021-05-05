
from django.contrib import admin
from django.urls import path
from main.views import main, page, contact
from shop.views import shop_list, save_product

urlpatterns = [
    path('', main),
    path('contact', contact),
    path('admin/', admin.site.urls),
    path('shop', shop_list),
    path('shop/save/product', save_product, name="save-product"),
    path('shop/filter/<int:cat_id>', shop_list, name='shop-filter'),
    path('<slug:page_name>', page),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

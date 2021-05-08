
from django.contrib import admin
from django.urls import path, include, re_path
from main.views import main, page, contact, set_locale
from shop.views import shop_list, save_product, add_to_cart
from account.views import register, cart, exit

from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('', main),
    path('contact', contact),
    path('set/locale/<str:locale>', set_locale),
    path('logout', exit),
    path('registration', register),
    path('admin/', admin.site.urls),
    path('shop', shop_list, name='shop-list'),
    path('cart', cart),
    path('shop/save/product', save_product, name="save-product"),
    path('add/to/cart/<int:product_id>', add_to_cart),
    path('shop/filter/<int:cat_id>', shop_list, name='shop-filter'),
    path('<slug:page_name>', page),
    re_path(r'^rosetta/', include('rosetta.urls'))
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

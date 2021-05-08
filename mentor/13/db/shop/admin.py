from django.contrib import admin
from .models import Category, Product, Product2User
# Register your models here.
from modeltranslation.admin import TranslationAdmin


class CategoryAdmin(TranslationAdmin):
    list_display = ['name', 'test']
    
   
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
   
admin.site.register(Product, ProductAdmin)

class BasketAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']
   
admin.site.register(Product2User, BasketAdmin)
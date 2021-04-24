from django.contrib import admin
from .models import Category, Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
   
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
   
admin.site.register(Product, ProductAdmin)
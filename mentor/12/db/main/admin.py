from django.contrib import admin

# Register your models here.

from main.models import Page

class PageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Page, PageAdmin)


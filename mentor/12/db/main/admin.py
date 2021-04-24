from django.contrib import admin

# Register your models here.

from main.models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'alias', 'content', 'is_published']
    list_editable = ['is_published']
    search_fields = ['title']


admin.site.register(Page, PageAdmin)


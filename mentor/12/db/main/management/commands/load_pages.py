from django.core.management.base import BaseCommand
from main.models import Page

class Command(BaseCommand):
  
    def handle(self, *args, **options):
        print('loading pages....')
        Page.objects.all().delete()
        p = Page()
        p.title="Main page"
        p.alias="main"
        p.content = "Content" 
        p.save()

        p = Page()
        p.title="Contact page"
        p.content = "Content" 
        p.alias="contact"
        p.save()

        p = Page()
        p.title="Shop page"
        p.alias="shop"
        p.content = "Content" 
        p.save()
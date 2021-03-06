from django.db import models
from django.utils.html import mark_safe

from django.db.models.signals import pre_save
from django.dispatch import receiver
from shop.models import Category

@receiver(pre_save, sender=Category)
def handle_category(sender, **kwargs):
    print(sender)
    print(kwargs)
    print(kwargs['instance'])


class Page(models.Model):
    title = models.CharField(max_length=250)
    alias = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="pages", blank=True, null=True)
    is_published = models.BooleanField(default=False)

    @property
    def my_image(self):
        try:
            return mark_safe(f'<img width="100" src="{self.image.url}" />')
        except:
            return 'No image'

    def __str__(self):
        return self.title



# class Animal():
#     color = 'red'
#     def jump(self):
#         print(self.color)
#         print('Jump')

# class Dog(Animal):
#     def gav():
#         print('gav')
#     def jump(self):
#         pass

# dog = Dog()

# cat.jump()
# cat.color

# ./manage.py makemigrations
# ./manage.py migrate




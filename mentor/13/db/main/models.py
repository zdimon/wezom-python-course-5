from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=250)
    alias = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="pages", blank=True, null=True)
    is_published = models.BooleanField(default=False)

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


from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()

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



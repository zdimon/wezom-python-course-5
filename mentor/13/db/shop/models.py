from django.db import models
from account.models import Account
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)
    test = models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return self.name   

    def save(self, *args, **kwargs):
        self.test = '%s (id: %s)' % (self.name, self.id)
        super(Category, self).save(*args, **kwargs)     

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return '%s (%s)' % (self.name, self.category) 

class Product2User(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)


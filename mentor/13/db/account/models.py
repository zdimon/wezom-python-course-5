from django.db import models
from django.contrib.auth.models import User

class Account(User):
    fullname = models.CharField(max_length=250, help_text="Enter you surname")
    phone = models.CharField(max_length=250)
    image = models.ImageField(upload_to='account')

    def __str__(self):
        return '%s (%s)' % (self.id, self.fullname) 



# Create your models here.

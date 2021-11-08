# from typing_extensions import Required
from django.db import models
from users.models import CustomUser
# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    writtentime = models.CharField(max_length=200)
    rentedtime = models.DateField(auto_now=True)
    image = models.CharField(max_length=300)
    rented = models.BooleanField(default=False)
    user = models.ManyToManyField(CustomUser)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
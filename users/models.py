from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    age = models.CharField(max_length=50)
    # add additional fields in here
    db_table = 'auth_user'
    
    def __str__(self):
        return self.username
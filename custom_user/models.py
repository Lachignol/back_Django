from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='profile_pict',blank=True,null=True)
    
    

    def __str__(self):
        return self.username
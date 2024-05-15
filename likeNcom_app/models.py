from django.db import models
from auth_app.models import User
# Create your models here.


class Like(models.Model):
    user= models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
     
     
    def __str__(self):
        return self.user.username
    

    
class Comment(models.Model):
    user= models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    content= models.TextField(max_length=255)
     
     
    def __str__(self):
        return self.user


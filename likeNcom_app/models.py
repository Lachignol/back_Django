from django.db import models
from auth_app.models import User
from food_app.models import Restaurant
# Create your models here.



    
class Comment(models.Model):
    user= models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    content= models.TextField(max_length=255)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
     
     
    def __str__(self):
        
        return "Commentaire de  %s sur le restaurant  %s." % (self.user.username,self.restaurant.name)
    


from django.db import models;
from auth_app.models import User
from likeNcom_app.models import Like,Comment

    
    
class Food_type(models.Model):
    name=models.CharField(max_length=150,)
    
    
    
    
    
    def __str__(self):
        return self.name



class Inclusive_type(models.Model):
    name=models.CharField(max_length=150,)
    
    
    
    
    
    def __str__(self):
        return self.name
    
    
    
    
class Restaurant(models.Model):
    name=models.CharField(max_length=150,)
    adress=models.CharField(max_length=150,)
    price=models.FloatField(null=True, blank=True,default=0)
    creator=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    inclusive_type=models.ForeignKey(Inclusive_type,on_delete=models.SET_NULL,null=True)
    food_type=models.ForeignKey(Food_type,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(upload_to='restaurant_pict',blank=True,null=True)
    likes = models.ManyToManyField(Like)
    comments = models.ManyToManyField(Comment)
    
    

    def __str__(self):
        return self.name
    
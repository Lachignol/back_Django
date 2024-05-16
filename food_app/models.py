from django.db import models;
from auth_app.models import User



    
    
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
    likes = models.ManyToManyField(User,related_name="restaurant_post",blank=True,default="")

    
    

    def __str__(self):
        return self.name
    
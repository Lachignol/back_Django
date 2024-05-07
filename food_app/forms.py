from django.forms import ModelForm
from django import forms
from .models import Restaurant

class RestaurantForm(ModelForm):

    
    class Meta:
        model = Restaurant 
        fields = ['name','adress','price','inclusive_type','food_type','image']
        
       
                
class RestaurantUpdateForm(ModelForm):

    
    class Meta:
        model = Restaurant 
        fields = ['name','adress','price','inclusive_type','food_type','image']
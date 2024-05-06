from django.forms import ModelForm
from django import forms
from .models import Restaurant

class RestaurantForm(ModelForm):
 
    
    class Meta:
        model = Restaurant 
        fields = '__all__'
        exclude = ('creator',)
       
                

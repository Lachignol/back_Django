from django.forms import ModelForm
from django import forms

from .models import User



class UserLoginForm(ModelForm):
    username = forms.CharField(required=True)
    
    class Meta:
        model = User 
        fields = ['username','password']
        
        


class UserSignUpForm(ModelForm):
    
    
    class Meta:
        first_name = forms.CharField(required=True)
        last_name = forms.CharField(required=True)
        email = forms.EmailField(required=True, max_length=100)
        password = forms.CharField(widget=forms.PasswordInput)
        model = User 
        fields = ['username','first_name','last_name','email','password','avatar']
        widgets = {
            'password': forms.PasswordInput(),
        }
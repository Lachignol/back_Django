from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import SetPasswordForm

from django.contrib.auth.forms import UserCreationForm

from .models import User



class UserLoginForm(ModelForm):
    username = forms.CharField(required=True)
    
    class Meta:
        model = User 
        fields = ['username','password']
        widgets={
            'password':forms.PasswordInput()
        }
                
        


class UserSignUpForm(UserCreationForm):
    
    
    class Meta:
        first_name = forms.CharField(required=True)
        last_name = forms.CharField(required=True)
        email = forms.EmailField(required=True, max_length=100)
        password = forms.CharField(label='Password', widget=forms.PasswordInput)
        password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)
        model = User 
        fields = ['username','first_name','last_name','email','avatar']
        widgets = {
            'password': forms.PasswordInput(),
        }
        
       
       
class UserUpdateForm(ModelForm):
    
    
    class Meta:
        first_name = forms.CharField(required=True)
        last_name = forms.CharField(required=True)
        email = forms.EmailField(required=True, max_length=100)
        password = forms.CharField(label=("Password"),
        help_text=("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but yeretertertertertretertou can change the password "
                    "using <a href=\"../password/\">this form</a>."))

        model = User 
        fields = ['username','first_name','last_name','email','avatar',]
        
        
        



class PasswordChangeForm(SetPasswordForm):
    pass
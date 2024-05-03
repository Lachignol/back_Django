from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
# from .forms import UserLoginForm, UserSignUpForm
from django.contrib import messages

from .forms import RestaurantForm
from .templates import *
from .models import Restaurant,Food_type,Inclusive_type

# Create your views here.

def allRestaurants(request):
    
    
    allRestaurants = Restaurant.objects.all()
    
    
    context={
        "allRestaurants":allRestaurants
    }

    return render(request,'food_app/allRestaurants.html',context)




def addRestaurant(request):
    if request.method == "POST" :
                form = RestaurantForm(request.POST)
                
                if form.is_valid():
                 userForm = form.save(commit=False)
                return HttpResponseRedirect("bien ajouté")
                context={
                "User":user,
                }
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL,context)
        # else:
        #         context={
        #         "form":UserLoginForm(),
               
        #         }
        #         messages.error(request, "Mauvais identifiant")
        #         return render(request,"auth_app/login.html",context) 
    if request.method == "GET" : 
            form = RestaurantForm()
            return render(request,"food_app/editRestaurant.html",{'form':form}) 
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
# from .forms import UserLoginForm, UserSignUpForm
from django.contrib import messages

from auth_app.models import User

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

def oneRestaurant(request,restaurantId):
    restaurant = Restaurant.objects.get(pk=restaurantId)
    context={
        "restaurant":restaurant
    }
    return render(request,'food_app/oneRestaurant.html',context)


def addRestaurant(request):
    if request.method == "POST" :
                form = RestaurantForm(request.POST,request.FILES)
                if form.is_valid():
                 restaurant = form.save(commit=False)
                 print(request.user)
                 restaurant.creator = request.user
                 restaurant.save()
                 messages.success(request, f"{restaurant.name} bien ajouté")
                return HttpResponseRedirect("/food/all")
    if request.method == "GET" : 
            form = RestaurantForm()
            return render(request,"food_app/editRestaurant.html",{'form':form}) 
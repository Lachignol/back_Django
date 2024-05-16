from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from food_app.models import Restaurant
from .models import *

# Create your views here.



def addOrDeleteLike(request,restaurantId):
    if request.method == "POST" :
        if request.user.is_authenticated:
            user = request.user
            restaurant = Restaurant.objects.get(pk=restaurantId)
            print(restaurant)
            print("tchikec",restaurant.likes)
        if restaurant.likes.filter(id=user.id).exists():
            restaurant.likes.remove(user)
        else : 
            restaurant.likes.add(user)
        return HttpResponseRedirect(reverse("food_app:one_restaurant", kwargs={"restaurantId":restaurantId}))
    else :
        return HttpResponseRedirect(reverse("food_app:one_restaurant",kwargs={"restaurantId":restaurantId}))  


def addOrDeleteLike(request,restaurantId):
    if request.method == "POST" :
        if request.user.is_authenticated:
            user = request.user
            restaurant = Restaurant.objects.get(pk=restaurantId)
            print(restaurant)
            print("tchikec",restaurant.likes)
        if restaurant.likes.filter(id=user.id).exists():
            restaurant.likes.remove(user)
        else : 
            restaurant.likes.add(user)
        return HttpResponseRedirect(reverse("food_app:one_restaurant", kwargs={"restaurantId":restaurantId}))
    else :
        return HttpResponseRedirect(reverse("food_app:one_restaurant",kwargs={"restaurantId":restaurantId})) 
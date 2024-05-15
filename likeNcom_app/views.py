from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from food_app.models import Restaurant
from .models import *

# Create your views here.



def addOrDeleteLike(request,restaurantId):
    if request.method == "POST" :
        restaurant = Restaurant.objects.get(pk=restaurantId)
        print("tchikec",restaurant.likes.filter(user=request.user))
        if like := restaurant.likes.filter(user=request.user):
            like.delete()
        else : 
            restaurant.likes.add(Like.objects.create(user=request.user))
        return HttpResponseRedirect(reverse("food_app:one_restaurant", kwargs={"restaurantId":restaurantId}))
    else :
        return HttpResponseRedirect(reverse("food_app:one_restaurant",kwargs={"restaurantId":restaurantId}))  

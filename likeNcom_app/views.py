from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from food_app.models import Restaurant
from .models import *

# Create your views here.



def addOrDeleteLike(request,restaurantId):

    restaurant = Restaurant.objects.get(pk=restaurantId)
    print(restaurant.likes)
    # if like := restaurant.likes.user == user:
    #     like.delete()
    # else : 
    restaurant.likes.add(Like.objects.create(user=request.user))
    return HttpResponseRedirect("one_restaurant")  

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
# from .forms import UserLoginForm, UserSignUpForm
from django.contrib import messages

from auth_app.models import User
from likeNcom_app.models import Comment

from .forms import RestaurantForm, RestaurantUpdateForm
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
    commentaires = Comment.objects.filter(restaurant=restaurant)
    context={
        "restaurant":restaurant,
        "commentaires":commentaires
    }
    return render(request,'food_app/oneRestaurant.html',context)

def restaurantsOfUser(request):
    if request.method == "GET" :
                 restaurants = Restaurant.objects.filter(creator=request.user)
                 context={
                  "restaurantsOfUser":restaurants
                 }
                 return render(request,"food_app/restaurantsOfUser.html",context)


def addRestaurant(request):
    if request.method == "POST" :
                form = RestaurantForm(request.POST,request.FILES)
                if form.is_valid():
                   restaurant = form.save(commit=False)
                   restaurant.creator = request.user
                   restaurant.save()
                   messages.success(request, f"{restaurant.name} bien ajouté")
                   return HttpResponseRedirect("/food/all") 
    else:
     form = RestaurantForm()
    return render(request,"food_app/addRestaurant.html",{'form':form}) 



def updateRestaurant(request,restaurantId):
        restaurantInit = Restaurant.objects.get(pk=restaurantId)
        if request.method == "POST":
                  
                  form = RestaurantUpdateForm(request.POST,request.FILES, instance=restaurantInit)
                  if form.is_valid():
                   restaurant = form.save()
                   restaurant.creator = request.user
                   restaurant.save()
                  return HttpResponseRedirect("/food/restaurantsOfUser")
        else :
                form = RestaurantUpdateForm(instance=restaurantInit)   
                context = {
                "form":form
                ,}
                return render(request, 'food_app/updateRestaurant.html', context)
        
        
def deleteRestaurant(request,restaurantId):
    if request.method == "POST" :
                 restaurant = Restaurant.objects.get(pk=restaurantId)
                 if request.user == restaurant.creator :
                   restaurant.delete()
                   messages.info(request, f"{restaurant.name} bien supprimé")
    return HttpResponseRedirect("/food/restaurantsOfUser")


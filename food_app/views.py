from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from auth_app.models import User
from likeNcom_app.forms import CommentForm
from likeNcom_app.models import Comment
from .forms import RestaurantForm, RestaurantUpdateForm
from .templates import *
from .models import Restaurant

# Create your views here.

def allRestaurants(request):
    allRestaurants = Restaurant.objects.all()
    context={
        "allRestaurants":allRestaurants
    }
    return render(request,'food_app/allRestaurants.html',context)

def oneRestaurant(request,restaurantId):
    user=request.user
    restaurant = Restaurant.objects.get(pk=restaurantId)
    commentaires = Comment.objects.filter(restaurant=restaurant)
    likeStatus = restaurant.likes.filter(id=user.id).exists()
    print(likeStatus)
    form = CommentForm()
    context={
        "restaurant":restaurant,
        "commentaires":commentaires,
        'form':form,
        'like':likeStatus
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
                   return HttpResponseRedirect("/all") 
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
                  return HttpResponseRedirect("/restaurantsOfUser")
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
    return HttpResponseRedirect("/restaurantsOfUser")


from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from food_app.models import Restaurant
from .forms import *
from .models import *

# Create your views here.



def addComment(request,restaurantId):
    restaurant = Restaurant.objects.get(pk=restaurantId)
    if request.method == "POST" :
                form = CommentForm(request.POST,request.FILES)
                if form.is_valid():
                   comment = form.save(commit=False)
                   comment.user = request.user
                   comment.restaurant = restaurant
                   comment.save()
                   messages.success(request, f"commentaire de {comment.user} bien ajouté")
    return HttpResponseRedirect(reverse("food_app:one_restaurant", kwargs={"restaurantId":restaurantId}))
 


def deleteComment(request,restaurantId,commentId):
    comment = Comment.objects.get(pk=commentId)
    if request.user == comment.user :
        comment.delete()
        messages.info(request, f" message de {comment.user} bien supprimé")
    return HttpResponseRedirect(reverse("food_app:one_restaurant", kwargs={"restaurantId":restaurantId}))




def addOrDeleteLike(request,restaurantId):
    if request.method == "POST" :
        if request.user.is_authenticated:
            user = request.user
            restaurant = Restaurant.objects.get(pk=restaurantId)
        if restaurant.likes.filter(id=user.id).exists():
            restaurant.likes.remove(user)
        else : 
            restaurant.likes.add(user)
        return HttpResponseRedirect(reverse("food_app:one_restaurant", kwargs={"restaurantId":restaurantId}))
    else :
        return HttpResponseRedirect(reverse("food_app:one_restaurant",kwargs={"restaurantId":restaurantId})) 
from django.urls import path
from .views import *

app_name='food_app'


urlpatterns = [
    path('all',allRestaurants,name="all_restaurants"),
    path('add',addRestaurant,name="add_restaurant"),
    path('one/<int:restaurantId>/',oneRestaurant,name="one_restaurant"),
    path('updateRestaurant/<int:restaurantId>/',updateRestaurant,name="update_restaurant"),
    path('restaurantsOfUser/',restaurantsOfUser,name="restaurantsOfUser"),
    path('deleteRestaurant/<int:restaurantId>/',deleteRestaurant,name='restaurant_delete')
    # path('restaurantsby/<str:food_type>/',restaurantByCateg,name="restaurant_by_food_type")
]
from django.urls import path
from .views import *

app_name='food_app'


urlpatterns = [
    path('all',allRestaurants,name="all_restaurants"),
    path('edit',addRestaurant,name="add_restaurant"),
    path('one/<int:restaurantId>/',oneRestaurant,name="one_restaurant"),
    path('restaurantsOfUser/',restaurantsOfUser,name="restaurantsOfUser")
    # path('restaurantsby/<str:food_type>/',restaurantByCateg,name="restaurant_by_food_type")
]
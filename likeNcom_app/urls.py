from django.urls import path
from .views import *

app_name='likeNcom_app'

urlpatterns = [
  path('addOrDeleteLike/<int:restaurantId>/',addOrDeleteLike,name="addOrDelete_like"),
]

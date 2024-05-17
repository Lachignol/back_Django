from django.urls import path
from .views import *

app_name='likeNcom_app'

urlpatterns = [
  path('addOrDeleteLike/<int:restaurantId>/',addOrDeleteLike,name="addOrDelete_like"),
  path('addComment/<int:restaurantId>/',addComment,name="addComment"),
  path('deleteComment/<int:restaurantId>/<int:commentId>/',deleteComment,name="deleteComment")
]

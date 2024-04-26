from django.urls import path
from .views import *

urlpatterns = [
    path('signup',signUp,name="signup"),
    path('login', loginUser,name="login"),
    path('logout', logoutUser,name="logout")
]
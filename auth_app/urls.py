from django.urls import path
from .views import *

app_name='auth_app'


urlpatterns = [
    path('signup',signUp,name="signup"),
    path('login', loginUser,name="login"),
    path('logout', logoutUser,name="logout"),
    path('updateProfil/',updateUser,name="update_user"),
    path('delete/<int:userId>/',deleteUser,name="delete_user"),
    path('profil',profilUser,name="profil_user")
]
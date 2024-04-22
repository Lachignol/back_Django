from django.urls import path
from .views import signIn

urlpatterns = [
    path('signin', signIn,name="signin"),
]
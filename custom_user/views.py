from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from .templates import *
from .models import User


def signUp(request):
        if request.method == "POST" :
            print(f"dans le post")
            username = request.POST['username']
            password = request.POST['password']
            upload = request.FILES['avatar']
            fss = FileSystemStorage(location='media_files/profile_pict/',base_url='/profile_pict')
            file = fss.save(upload.name,upload)
            file_url = fss.url(file)
            print(file_url)
            user = User.objects.create_user(username=username,password=password,avatar=fss.url(file))
            user.save()
            login(request, user)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        if request.method == "GET":
            print(f"dans le Get")
            return render(request,'custom_user/signUp.html')


def loginUser(request):
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user.avatar)
        if user is not None and user.is_active:
            login(request, user)
            context={
                "User":user,
            }
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL,context)
    if request.method == "GET" : 
        
        if request.user.is_authenticated:
            context={
                "User":request.user,
            }
            return render(request,"custom_user/login.html",context) 
            
        else : 
            return render(request,"custom_user/login.html") 
            
    

def logoutUser(request):
        logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate,login,logout
from .forms import UserLoginForm, UserSignUpForm, UserUpdateForm
from django.contrib import messages
from .templates import *
from .models import User



def signUp(request):
        if request.method == "POST" :
            form = UserSignUpForm(request.POST,request.FILES)
            if form.is_valid():
                userForm = form.save(commit=False)
                user = User.objects.create_user(username=userForm.username,first_name=userForm.first_name,last_name=userForm.last_name,email=userForm.email,password=userForm.password,avatar=userForm.avatar)
                login(request, user)
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        if request.method == "GET":
            form = UserSignUpForm()
        return render(request,'auth_app/signup.html',{'form':form})


def loginUser(request):
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
                login(request, user)
                messages.success(request, f"{user.username} connecté")
                context={
                "User":user,
                }
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL,context)
        else:
                context={
                "form":UserLoginForm(),
               
                }
                messages.error(request, "Mauvais identifiant")
                return render(request,"auth_app/login.html",context) 
    if request.method == "GET" : 
            form = UserLoginForm()
            return render(request,"auth_app/login.html",{'form':form}) 
            
    

def logoutUser(request):
        logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)



def updateUser(request):
        if request.method == "POST":
                  form = UserUpdateForm(request.POST,request.FILES, instance=request.user)
                  if form.is_valid():
                   user = form.save()
                   login(request,user)
                  return HttpResponseRedirect("/auth/profil")
        else :
                form = UserSignUpForm(instance=request.user)   
                context = {
                "form":form
                ,}
                return render(request, 'auth_app/updateProfil.html', context)
    



def deleteUser(request,userId):
    if request.method == "POST" :
                 user = User.objects.get(pk=userId)
                 if request.user == user :
                   user.delete()
                   messages.info(request, f"{user.name} bien supprimé")
    return HttpResponseRedirect("/auth/signup")




def profilUser(request):
    return render(request, 'auth_app/profilPage.html')
       
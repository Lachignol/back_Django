from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from .forms import UserLoginForm, UserSignUpForm
from .templates import *
from .models import User







def signUp(request):
        if request.method == "POST" :
            print(f"dans le post")
            # username = request.POST['username']
            # password = request.POST['password']
            # upload = request.FILES['avatar']
            # fss = FileSystemStorage(location='media_files/profile_pict/',base_url='/profile_pict')
            # file = fss.save(upload.name,upload)
            # file_url = fss.url(file)
            # print(file_url)
            form = UserSignUpForm(request.POST,request.FILES)
            
           
            print("form valid ",form.is_valid())
            print(form.errors)
            if form.is_valid():
                userForm = form.save(commit=False)
                print(userForm.avatar)
                # if userForm.avatar:
                #         upload = userForm.avatar
                #         fss = FileSystemStorage(location='media_files/profile_pict/',base_url='/profile_pict')
                #         file = fss.save(upload.name,upload)
                #         file_url = fss.url(file)
                #         # upload = userForm.avatar
                #         print(userForm.avatar)
                #         print(userForm.username)
                #         print(userForm.first_name)
                #         print(userForm.last_name)
                #         print(userForm.email)
                user = User.objects.create_user(username=userForm.username,first_name=userForm.first_name,last_name=userForm.last_name,email=userForm.email,password=userForm.password,avatar=userForm.avatar)
                login(request, user)
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        if request.method == "GET":
            print(f"dans le Get")
            form = UserSignUpForm()
        return render(request,'auth_app/signUp.html',{'form':form})


def loginUser(request):
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            context={
                "User":user,
            }
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL,context)
        else:
            form = UserLoginForm()
            errorCredential="mauvais identifiant veuillez réessayez"
            
            return render(request,"auth_app/login.html",{'form':form,'errorCredential':errorCredential}) 
            
    if request.method == "GET" : 
        
        if request.user.is_authenticated:
            context={
                "User":request.user,
            }
            return render(request,"auth_app/login.html",context) 
            
        else : 
            form = UserLoginForm()
            return render(request,"auth_app/login.html",{'form':form}) 
            
    

def logoutUser(request):
        logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)
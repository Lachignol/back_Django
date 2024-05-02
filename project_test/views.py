from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from .templates import *


def index(request):
    # User= request.user
    # if request.user.is_authenticated:
    #     print(User)
    #     context={
    #     "User":User
    #     }
    #     return render(request,"index.html",context=context)
    # else:
        return render(request,"index.html")
    
     
    
    # return render(request,'index.html',context=context)
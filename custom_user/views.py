from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .templates import *
from .models import User


def signIn(request):
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
            print( username ,password,upload.name)
           
            
        
        if request.method == "GET":
            print(f"dans le Get")
            return render(request,'custom_user/signin.html')

from threading import local

from django.contrib import messages,auth
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from credentials.models import Department,Courses


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request,"detail.html")
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,"login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                return render(request,"register.html")
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                return render(request,"login.html")
                messages.info(request,"User created")


        else:
            messages.info(request,"Password not match")
            return render(request,"register.html")
        return redirect('/')
    return render(request,"register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def dept(request):
   dep=Department.objects.all()
   cou=Courses.objects.all()
   return render(request,"details.html",{'department':dep,'courses':cou})



def details(request):
    messages.success(request,"Successesfully  Recorded Your Previous Response")
    return render(request,"details.html")

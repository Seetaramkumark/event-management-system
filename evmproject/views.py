from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http import HttpResponse

def booking(request):
    return render(request,"booking.html")



def homepage(request):
    return render(request, "login.html")

def payment(request):
    return render(request, "payment.html")

def homepage1(request):
    return render(request, "signin.html")

def sucess(request):
    return render(request, "sucess.html")

def default1(request):
    return render(request, "index.html")


def usereventsfunction(req):
    return render(req, "events.html")

def userhomefunction(req):
    return render(req, "userhome.html")

def userordersfunction(req):
    return render(req , "userorders.html")

def userfeedbackfunction(req):
    return render(req , "userfeedback.html")

def contactrequest(request):
    return render(request , "request.html")


def htmlpage(request):
    return render(request , "html.html")
def logout(request):
    auth.logout(request)
    return redirect("/")


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print("yes")
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, 'login.html')




def signin(request):
    if request.method == 'POST':

        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        print(username, email, password, cpassword)
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request,"User already exists")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.error(request,"Email already exists")
                return redirect("signin")
            else:
                user=User.objects.create_user(username=username, email=email, password=password)
                user.save()
                print("User created")
                return redirect('login')
        else:
            messages.error(request,"Password not matching ...")
            return redirect("signin")
    return render(request,'signin.html')
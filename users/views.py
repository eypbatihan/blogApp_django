from django.shortcuts import redirect, render
from .forms import UserForm,ProfileForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def home(request):
    return render(request,"users/home.html")

def register(request):
    form = UserForm()
    if request.method =="POST":
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect("home")
    context = {
        "form_user":form
    }
    return render(request,"users/register.html",context) 
 


def user_logout(request):
    logout(request)
    return render(request,"users/logout.html") 



def user_login(request):
    form =AuthenticationForm(request.POST,data=request.POST)
    if form.is_valid():
        user = form.get_user()
        if user:
            login(request,user)
            return redirect("home")
    context = {
        "form":form
    }
    return render(request,"users/login.html",context)


def profile(request):
    user = request.user
    form = ProfileForm(instance =user)
    if request.method =="POST":
        form = UserForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {
        "form":form,
        "user":user,
    }
    return render(request,"users/profile.html",context) 

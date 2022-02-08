from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Blog

from .forms import BlogForm

# Create your views here.
def post_create(request):
    post_form = BlogForm()
    if request.method =="POST":
        post_form = BlogForm(request.POST,request.FILES)
        # print(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect("home")

    context = {
        "post_form":post_form
    }
    return render(request,"blog/post_create.html",context)

def post_list(request):
    blogs=Blog.objects.all()
    context={
        "blogs":blogs
    }
    return render(request,"users/home.html",context)
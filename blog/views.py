from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Like, PostView
import os

from .forms import BlogForm, CommentForm



# Create your views here.


def post_create(request):
    post_form = BlogForm() 
    if request.method == "POST":
        post_form = BlogForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.instance.user = request.user
            post_form.save()
            return redirect("home")
    context = {
        "post_form": post_form,  
    }
    return render(request, "blog/post_create.html", context)



def post_list(request):
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs
    }
    return render(request, "users/home.html", context)


def post_details(request, id):
    blog = Blog.objects.get(id=id)
    form = CommentForm()
    if request.user.is_authenticated:
        view_qs = PostView.objects.filter(user=request.user,post=blog)
        if not view_qs:
            PostView.objects.create(user =request.user,post=blog)
        if request.method=='POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.post = blog
                comment.save()
                return redirect("details",id=id)
    context = {
        "blog":blog,
        "form":form,
    }

    return render(request, "blog/post_details.html",context)


def post_update(request, id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(instance=blog)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {
        "blog": blog,
        "form": form,
    }
    return render(request, "blog/post_update.html", context)


def post_delete(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == "POST":
        if blog.Image:
            blog.Image.delete()
        blog.delete()
        return redirect("home")
    return render(request, "blog/post_delete.html", {"blog": blog})

def post_like(request,id):
     if request.user.is_authenticated:
         if request.method == "POST":
             blog = Blog.objects.get(id=id)
             like_qs = Like.objects.filter(user=request.user,post=blog)
             if like_qs:
                like_qs[0].delete()
             else:
                Like.objects.create(user =request.user,post=blog)
     return redirect("details",id=id)


   

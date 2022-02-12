from django.shortcuts import redirect, render
from .models import Blog


from .forms import BlogForm



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
    return render(request, "blog/post_details.html", {"blog": blog})


def post_update(request, id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(instance=blog)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.owner = request.user
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
        blog.delete()
        return redirect("home")
    return render(request, "blog/post_delete.html", {"blog": blog})

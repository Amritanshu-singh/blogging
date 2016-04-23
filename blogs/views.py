from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect

# Create your views here.
from .forms import PostForm
from .models import Post


def blog_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())

    #if request.method == "POST":
        #print request.POST.get("content")
        #print request.POST.get("title")

    context = {
        "form": form,


    }
    return render(request, "post_form.html", context)

def blog_details(request, id = None):
    instance = get_object_or_404(Post, id = id)
    context = {
        "title" : instance.title,
        "instance" : instance

    }
    return render(request, "post_detail.html", context)

def blog_list(request):
    queryset = Post.objects.all()
    #return HttpResponse("<h1>List</h1>")
    context = {
        "object_list": queryset,
        "title" : "List"

    }
    return render(request, "index.html", context)
def blog_update(request, id =None):

    instance = get_object_or_404(Post, id = id)
    form = PostForm(request.POST or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit= False)
        instance.save()

        messages.success(request, "Saved ")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title":instance.title,
        "instance":instance,
        "form": form,

    }
    return render(request, "post_form.html", context)

def blog_delete(request, id =None):
    instance = get_object_or_404(Post, id = id)
    instance.delete()
    messages.success(request, "Successfully Deleted ")
    return redirect("post_list")

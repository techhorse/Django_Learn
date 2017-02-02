from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post

# Create your views here.
def post_create(request):
    context = {
        "title":"Create",
    }
    return render(request,"index.html",context)

def post_detail(request):
    context = {
        "title":"Details",
    }
    return render(request,"index.html",context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "title":"List",
    }
    return render(request,"index.html",context)

def post_update(request):
    context = {
        "title":"Update",
    }
    return render(request,"index.html",context)

def post_delete(request):
    context = {
        "title":"Delete",
    }
    return render(request,"index.html",context)
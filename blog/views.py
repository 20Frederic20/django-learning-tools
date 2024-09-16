from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request,'blog/index.html',{'posts':posts})

def create(request):
    context={}
    template_name=''
    return render(request,template_name,context)

def show(request, uuid):
    post = get_object_or_404(Post, uuid=uuid)
    context={"post":post}
    template_name=''
    return render(request,template_name,context)

def update(request, uuid):
    post = get_object_or_404(Post, uuid=uuid)
    context={"post":post}
    template_name=''
    return render(request,template_name,context)

def delete(request, uuid):
    post = get_object_or_404(Post, uuid=uuid)
    context={"post":post}
    template_name=''
    return render(request,template_name,context)

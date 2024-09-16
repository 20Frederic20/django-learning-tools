from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):
    context={}
    template_name=''
    return render(request,template_name,context)

def create(request):
    context={}
    template_name=''
    return render(request,template_name,context)

def show(request, uuid):
    context={}
    template_name=''
    return render(request,template_name,context)

def update(request, uuid):
    context={}
    template_name=''
    return render(request,template_name,context)

def delete(request, uuid):
    post = get_object_or_404(Post, uuid=uuid)
    context={}
    template_name=''
    return render(request,template_name,context)

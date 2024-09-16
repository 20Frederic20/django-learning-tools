from django.shortcuts import render
import time

# Create your views here.


def index(request):
    time.sleep(0.5)
    if request.htmx:
        return render(request, 'blogs/index.html')
    else:
        return render(request, 'blogs/index.html')
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Rescue_Time_Query
from .rescue_time import execute
import time

# Create your views here.




def home(request):
    """ Routes traffic"""
    context = {
        'posts':Post.objects.all(),
        'title':'Homepage'
    }

    return render(request, 'blog/home.html', context)

def about(request):
    """ Routes traffic"""

    context = {
        'queries':Rescue_Time_Query.objects.all()
    }
    print(context)
    return render(request, 'blog/about.html', context)

def reload(request):
    """ Routes traffic"""
    execute()
    print("Executed")
    context = {
        'queries':Rescue_Time_Query.objects.all()
    }
    return render(request, 'blog/about.html', context)

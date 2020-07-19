from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


posts = [
    {
        'author': 'James Salafatinos',
        'title': 'blog post 1',
        'content': 'My content',
        'date_posted':'July 17th, 2020'
    },
    {
        'author': 'James Salvo',
        'title': 'blog post 2',
        'content': 'My content',
        'date_posted':'July 17th, 2020'
    }
]

def home(request):
    """ Routes traffic"""
    context = {
        'posts':posts,
        'title':'Homepage'
    }

    return render(request, 'blog/home.html', context)

def about(request):
    """ Routes traffic"""
    return render(request, 'blog/about.html', {'title':'About'})

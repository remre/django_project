from django.shortcuts import render
from django.http import HttpResponse

posts = [

    {
        'author': "Coreym",
        'title': 'Blog Post',
        'content': 'First post content',
        'date_posted':'November 10 2021'

    },
    
    {
        'author': "Coreysm",
        'title': 'Blog Post2',
        'content': 'Second post content',
        'date_posted':'November 11 2021'

    }
    
]

def home(request):
    #we add context and sync it with posts
    context = {
        'addings': posts,
            }
    return render(request,'C:/Users/emreb/Documents/djangoyoutubeproject/django_project/blog/templates/blog/home.html',context)#using httpResponse to handle the traffic on home page 

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

#we will load our templates and django provides us a shortcut as u can see render did it for us 
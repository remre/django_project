from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

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
        'addings': Post.objects.all(),
            }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

#we will load our templates and django provides us a shortcut as u can see render did it for us 
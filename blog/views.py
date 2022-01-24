from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView , DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Post
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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
    template_name= 'blog/home.html'
    context_object_name = 'addings'
    
    paginate_by = 6

class UserPostListView(ListView):
    model = Post
    template_name= 'blog/user-posts.html'
    context_object_name = 'addings'
    ordering = ['-date_posted'] 
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('date_posted')
        # popular_events = Events.objects.annotate(attendee_count=Count('attendee')).filter(attendee_count__gt=50)



 # def get_queryset(self):
    #     person = get_object_or_404(person, username=self.kwargs.get('username'))
    #     # original qs
        # qs = super().get_queryset()
        # filter by a variable captured from url, for example
        # Salon.objects.filter(author=person).order_by('-date_posted')
        # qs.filter(name__startswith=self.kwargs['name'])


    

       



class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Post
    fields = ['title', 'content']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user  == post.author:
            return True
        messages.error(
            self.request, 'You do not have permission to view the previous page.')
        return False 

        

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'



    def test_func(self):
        post = self.get_object()
        if self.request.user  == post.author:
            return True
        messages.error(
            self.request, 'You do not have permission to view the previous page.')

        return False

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

#we will load our templates and django provides us a shortcut as u can see render did it for us 
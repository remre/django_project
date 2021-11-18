from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),#we add our home page on views there 

    path('about/', views.about, name='blog-about'),
    #path('login/', views. )

]

#so we update views.home oart as PostListView and now home page url wants to reach template like blog/post_list.html 
# <app>/<model>_<viewtype>.html

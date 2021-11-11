from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),#we add our home page on views there 
    path('about/', views.about, name='blog-about'),
    #path('login/', views. )
]

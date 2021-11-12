from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()#we keep it default

    class Meta: #keep configuration in one place 
        model = User
        fields = ['username', 'email', 'password1', 'password2']
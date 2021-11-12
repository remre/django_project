from django.forms.widgets import EmailInput
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # we dont need it anymore 
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #email = EmailInput(request.POST)
        if form.is_valid():
            form.save() #if it is ok it will save it 
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
    # we will use classes already exists in django
        form  = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})
        




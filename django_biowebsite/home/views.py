from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import UserLoginForm

def home_view(request):
    return render(request, 'home/home.html')

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home:home')
    else:
        form = UserLoginForm()
    return render(request, 'home/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "You've been successfully logged out.")
    return redirect('home:home')

from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
import requests
from .models import Lesson

def lessons(request):
    lessons = Lesson.objects.all()
    return render(request, 'lessons.html', {'lessons': lessons})

def home(request):
    return render(request, 'home.html')

def logout(request):
    auth_logout(request)
    return redirect('home')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirect to the main page after successful login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to the main page after successful registration and login
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
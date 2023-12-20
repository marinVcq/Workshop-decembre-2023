from django.urls import path
from django.contrib import admin
from .views import home, login_view,logout, register, lessons

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
     path('lessons/', lessons, name='lessons'),
]

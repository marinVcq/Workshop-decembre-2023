from django.urls import path
from django.contrib import admin
from .views import home, login_view,logout, register, lessons, lesson_detail, complete_lesson, exercises, memory_rules,dashboard, start_memory_game, memorize_words, submit_answers

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('lessons/', lessons, name='lessons'),
    path('lesson/<int:lesson_id>/', lesson_detail, name='lesson_detail'),
    path('complete_lesson/<int:lesson_id>/', complete_lesson, name='complete_lesson'),
    path('exercises/', exercises, name='exercises'),
    path('memory/', memory_rules, name='memory_rules'),
    path('dashboard/', dashboard, name='dashboard'),
    path('memory/start/', start_memory_game, name='start_memory_game'),
    path('memory/memorize/', memorize_words, name='memorize_words'),
    path('memory/submit/', submit_answers, name='submit_answers'),

]

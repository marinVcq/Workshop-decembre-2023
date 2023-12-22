from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.http import HttpResponse
import requests
from .models import Lesson, CompletedLesson, ExerciseTheme
import random
import time

def dashboard(request):
    return render(request, 'dashboard.html')

def memory_rules(request):
    return render(request, 'memory/rules.html')

def start_memory_game(request):
    # Generate a list of 10 random words
    word_list = generate_random_words()
    
    # Store the word list in the session
    request.session['word_list'] = word_list
    random.shuffle(word_list)
    
    return redirect('memorize_words')

def memorize_words(request):
    # Assuming original_word_list is a list of words
    original_word_list = ["Pomme", "Banane", "Cerise", "Date", "Fraise"]

    # Make a copy of the original list and shuffle it
    shuffled_word_list = original_word_list.copy()
    random.shuffle(shuffled_word_list)

    # Pass both lists to the template
    context = {'original_word_list': original_word_list, 'shuffled_word_list': shuffled_word_list}
    return render(request, 'memory/memorize_words.html', context)

def submit_answers(request):
    # Get the word list from the session
    word_list = request.session.get('word_list', [])
    
    if not word_list:
        # Redirect to the start page if no word list found
        return redirect('start_memory_game')

    # Get user-submitted answers
    user_answers = request.POST.getlist('user_answer')

    # Check if the answers are correct
    correct = user_answers == word_list

    # Clear the word list from the session
    request.session['word_list'] = None

    return render(request, 'memory/submit_answers.html', {'correct': correct})


def generate_random_words():
    # Replace this with your own list of words
    all_words = ["apple", "banana", "cherry", "dog", "elephant", "flower", "guitar", "house", "ice cream", "jazz"]
    
    # Choose 10 random words
    word_list = random.sample(all_words, 10)
    
    return word_list

@login_required
def complete_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    user = request.user

    # Check if the user has already completed the lesson
    if not CompletedLesson.objects.filter(user=user, lesson=lesson).exists():
        # If not, create a new CompletedLesson record
        CompletedLesson.objects.create(user=user, lesson=lesson)

    return redirect('lesson_detail', lesson_id=lesson_id)

@login_required
def exercises(request):
    exercise_themes = ExerciseTheme.objects.all()
    return render(request, 'exercises.html', {'exercise_themes': exercise_themes})

@login_required
def lessons(request):
    user = request.user
    lessons = Lesson.objects.all()

    # Create a dictionary to store information about completed lessons
    completed_lessons_dict = {completed_lesson.lesson.id: completed_lesson for completed_lesson in CompletedLesson.objects.filter(user=user)}

    # Iterate through lessons and add 'user_completed_lesson' field
    for lesson in lessons:
        lesson.user_completed_lesson = completed_lessons_dict.get(lesson.id, None)

    return render(request, 'lessons.html', {'lessons': lessons})

@login_required
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    user = request.user

    user_completed_lesson = CompletedLesson.objects.filter(user=user, lesson=lesson).first()

    context = {'lesson': lesson, 'user_completed_lesson': user_completed_lesson}
    return render(request, 'lesson_detail.html', context)

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
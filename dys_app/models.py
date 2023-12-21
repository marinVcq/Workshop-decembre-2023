from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class MemoryGame(models.Model):
    words = models.TextField()

class ExerciseTheme(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Lesson(models.Model):
    SCHOOL_LEVEL_CHOICES = [
        ('Primaire', 'Primaire'),
        ('College', 'college'),
        ('Lycee', 'lycee'),
        ('superieur', 'superieur'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    publisher = models.CharField(max_length=255)
    youtube_link = models.URLField()
    school_level = models.CharField(max_length=20, choices=SCHOOL_LEVEL_CHOICES)

    def __str__(self):
        return self.title

class CompletedLesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'lesson'] 
# Generated by Django 4.2.7 on 2023-12-21 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dys_app', '0007_remove_lesson_completed_lessons'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseTheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
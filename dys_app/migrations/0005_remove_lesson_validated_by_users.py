# Generated by Django 4.2.7 on 2023-12-21 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dys_app', '0004_lesson_validated_by_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='validated_by_users',
        ),
    ]
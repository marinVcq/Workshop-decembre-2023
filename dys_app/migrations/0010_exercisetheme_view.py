# Generated by Django 4.2.7 on 2023-12-22 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dys_app', '0009_memorygame'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercisetheme',
            name='view',
            field=models.CharField(default='memory_rules', max_length=255),
        ),
    ]

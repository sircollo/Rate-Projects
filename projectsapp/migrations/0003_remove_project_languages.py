# Generated by Django 4.0.4 on 2022-06-12 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectsapp', '0002_project_poster_alter_profile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='languages',
        ),
    ]

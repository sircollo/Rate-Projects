# Generated by Django 4.0.4 on 2022-06-11 22:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('bio', models.TextField()),
                ('avatar', models.ImageField(default='image', upload_to='avatars/')),
                ('country', models.CharField(max_length=30)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('languages', models.CharField(choices=[('HT', 'html'), ('CS', 'css'), ('JS', 'javascript'), ('AG', 'angular'), ('FL', 'flask'), ('DJ', 'django')], default='HT', max_length=30)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='projectsapp.profile')),
            ],
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-12 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectsapp', '0010_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True, default='/', max_length=300),
        ),
    ]

from django.contrib import admin

from projectsapp.models import Profile
from .models import *
# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Rating)
admin.site.register(Category)
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.urls import reverse
from cloudinary.models import CloudinaryField
import cloudinary

# Create your models here.

class Profile(models.Model):
  name = models.CharField(max_length=30)
  bio = models.TextField()
  # avatar = models.ImageField(upload_to='avatars/',default='image')
  avatar = CloudinaryField('image')
  country = models.CharField(max_length=30)
  user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
  
  
  def __str__(self):
    return self.user.username
  
  def get_absolute_url(self):
    return reverse('index')
  
class Project(models.Model):
  name = models.CharField(max_length=30)
  description = models.TextField()
  LANGUAGES = [
    ('HTML','html'),
    ('CSS','css'),
    ('JAVASCRIPT','javascript'),
    ('ANGULAR','angular'),
    ('FLASK','flask'),
    ('DJANGO','django'),
          
  ]
  language = models.CharField(
    max_length=30,
    choices= LANGUAGES,
    default= 'HTML'
  )
  poster = cloudinary.models.CloudinaryField('image',default='image')
  upload_date = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True,related_name='project')
  
  def __str__(self):
    return self.name
  
  
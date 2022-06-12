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
  
class Category(models.Model):
  NAMES = [
    ('TECHNOLOGY', 'TECHNOLOGY'),
    ('SOCIAL', 'SOCIAL'),
    ('NEWS', 'NEWS'),
    ('SPORTS', 'SPORTS'),
    ('FASHION', 'FASHION'),

  ]
  name = models.CharField(choices=NAMES,max_length=30,default='TECHNOLOGY')
  
  def __str__(self):
    return self.name
  
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
  category = models.ManyToManyField(Category, related_name='projects')
  user = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True,related_name='project')
  url = models.URLField(max_length=300,default='/',blank=True)
  def __str__(self):
    return self.name
  
class Rating(models.Model):
  comment = models.TextField()
  project = models.ForeignKey(Project,on_delete=models.CASCADE, related_name='ratings')
  user = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='ratings')
  rating_date = models.DateTimeField(auto_now_add=True)
  RATINGS = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
  ]
  design = models.IntegerField(choices=RATINGS,default=0,blank=True)
  usability = models.IntegerField(choices=RATINGS,default=0,blank=True)
  content = models.IntegerField(choices=RATINGS,default=0,blank=True)
  design_average = models.FloatField(default=0)
  usability_average = models.FloatField(default=0)
  content_average = models.FloatField(default=0)
  
  def __str__(self):
    return self.comment
  
  
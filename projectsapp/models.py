from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Profile(models.Model):
  name = models.CharField(max_length=30)
  bio = models.TextField()
  avatar = models.ImageField(upload_to='avatars/')
  country = models.CharField(max_length=30)
  user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
  
  
  def __str__(self):
    return self.name
  
class Project(models.Model):
  name = models.CharField(max_length=30)
  description = models.TextField()
  HTML = 'HT'
  CSS = 'CS'
  JAVASCRIPT = 'JS'
  ANGULAR = 'AG'
  FLASK = 'FL'
  DJANGO = 'DJ'
  LANGUAGES = [
    (HTML,'html'),
    (CSS,'css'),
    (JAVASCRIPT,'javascript'),
    (ANGULAR,'angular'),
    (FLASK,'flask'),
    (DJANGO,'django'),
          
  ]
  languages = models.CharField(
    max_length=30,
    choices= LANGUAGES,
    default= HTML,
  )
  upload_date = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True,related_name='project')
  
  def __str__(self):
    return self.name
  
  
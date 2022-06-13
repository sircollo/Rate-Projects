from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ('id', 'name', 'bio','avatar','country','user')
    
class ProjectsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ('name','description','poster','language','url','category','total_ratings','design_average','usability_average','content_average')
    
class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rating
    fields = '__all__'
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from projectsapp.models import Profile, Project,Rating


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='username', max_length=50, widget=forms.TextInput(attrs={'placeholder':'Username'}), required=True)
    email = forms.EmailField(label='email', widget=forms.TextInput(attrs={'placeholder':'Email'}), required=True)
    password1 = forms.CharField(label='password', max_length=50, widget=forms.PasswordInput(attrs={'placeholder':'Password'}), required=True)
    password2 = forms.CharField(label='password', max_length=50, widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}), required=True)
    
    
class LoginForm(AuthenticationForm): 
  username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'})) 
  password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
  class Meta:
    model = User
    fields = ['username','password']
    
    
class CreateProfileForm(forms.ModelForm):
  name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'})) 
  country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Country'}))
  avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
  class Meta:
    model = Profile
    fields = '__all__'
    
class UpdateProfileForm(forms.ModelForm):
  name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'})) 
  country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Country'}))
  avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
  bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Tell us about yourself...'})) 
  class Meta:
    model = Profile
    fields = ['name','country','avatar','bio']
    
class ProjectUploadForm(forms.Form):
  name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Project Name'})) 
  description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Describe your project...'}))  
  LANGUAGES = [
    ('HTML','html'),
    ('CSS','css'),
    ('JAVASCRIPT','javascript'),
    ('ANGULAR','angular'),
    ('FLASK','flask'),
    ('DJANGO','django'),
          
  ]
  language = forms.ChoiceField(choices=LANGUAGES)
  poster =forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control','placeholder':'Upload File'}))
  class Meta:
    model = Project
    fields =['name','description','poster','language']
    
class ProjectRatingForm(forms.Form):
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
  design = forms.ChoiceField(choices=RATINGS)
  usability = forms.ChoiceField(choices=RATINGS)
  content = forms.ChoiceField(choices=RATINGS)
  comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Write you review...','width':'20px'}))
  class Meta:
    model = Rating
    fields = ['comment','design','usability','content']
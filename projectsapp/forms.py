from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from projectsapp.models import Profile


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='username', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}), required=True)
    email = forms.EmailField(label='email', widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}), required=True)
    password1 = forms.CharField(label='password', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}), required=True)
    password2 = forms.CharField(label='password', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirm Password'}), required=True)
    
    
class LoginForm(AuthenticationForm): 
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'})) 
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Password'}))
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
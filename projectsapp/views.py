import email
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,reverse,HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from .models import *
from django.views.generic.edit import View
from django.contrib import messages
from django.views.generic import ListView,CreateView
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
  return render(request, 'index.html')

def signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('signin')
    else:
     messages.warning(request,'Password Mismatch')
      
  form = SignUpForm()
  return render(request=request, template_name='registration/register.html',context={'form':form})

def signin(request):
  if request.method == 'POST':
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(request, username=username,password=password)
      if user is not None:
        login(request,user)
        return redirect('index')
      else:
        messages.error(request,'Invalid username or password')
        
    else:
      messages.error(request,'Invalid username or password')
  form = LoginForm()
  return render(request,'registration/login.html',{'form':form})

class SignOutView(View):
  def get(self,request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
  
class CreateProfileView(CreateView):
  model = Profile
  form_class = CreateProfileForm
  template_name = 'create_profile.html'
  
  def form_valid(self,form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
def profile(request,id):
  user = request.user
  profiles=Profile.objects.get(user=id)
  context = {'profiles':profiles}
  return render(request, 'profile.html', context)
      

def updateProfile(request,id):
  profile = Profile.objects.get(user=id)
  form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
  if request.method == 'POST':
    if form.is_valid():
      form.save()
      return redirect('profile',id)
  context = {'form':form}
  return render(request,'update_profile.html',context)
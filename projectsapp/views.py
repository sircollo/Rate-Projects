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
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from rest_framework import status
# Create your views here.

def home(request):
  projects = Project.objects.all()
  ratings = Rating.objects.all()
  
  # projects = request.get('127.0.0.1/api/profiles/').json()
  context = {'projects':projects,'ratings':ratings}
  return render(request, 'index.html',context)

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
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return redirect('index')
  
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

def uploadProject(request,id):
  profile = Profile.objects.get(user=id)
  user = request.user
  u_form = ProjectUploadForm(request.POST,request.FILES)
  print('no')
  if request.method == 'POST':
    if u_form.is_valid():    
      name = u_form.cleaned_data.get('name') 
      description = u_form.cleaned_data.get('description')
      poster = u_form.cleaned_data.get('poster') 
      # languages = u_form.request.GET('languages') 
      new_project = Project(name=name,description=description,poster=poster,user=profile)
      new_project.save()
      return redirect('index')
  context = {'form':u_form}
  return render(request,'project_upload.html',context)

class search_user(ListView):
  model= User,Profile
  template_name = 'user_search.html'
  
  def get_queryset(self):
    query = self.request.GET.get('search_user')
    object_list = User.objects.filter(
      Q(username__icontains=query)
    
    )
    # if not search_user
    return object_list
  
class ProfileList(APIView):
  def get(self, request, format=None):
    all_profiles = Profile.objects.all()
    serializers = ProfileSerializer(all_profiles, many=True)
    print(serializers.data)
    profiles = serializers.data
    # return render(request, 'index.html',{'profiles':profiles})
    return Response(serializers.data)
  
  
  def post(self, request, format=None):
    serializers = ProfileSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data,status=status.HTTP_201_OK)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


def review(request,id):
  user = request.user
  # profiles = Profile.objects.get(user=id)
  # print(profiles)
  project = Project.objects.get(id=id)
  user = Profile.objects.get(user=user)
  ratings = Rating.objects.get(project=project)
  form = ProjectRatingForm(request.POST)
  if request.method == 'POST':
    if form.is_valid():
      design = form.cleaned_data['design']
      usability = form.cleaned_data['usability']
      content = form.cleaned_data['content']
      comment = form.cleaned_data['comment']  
      da = float(design)
      x = (da/10)    
      new_rating = Rating(design=design,usability=usability,content=content,comment=comment,user=user,project=project,design_average=x)
      new_rating.save()
      
      return redirect('index')
  context = {'form':form,'project':project,'user':user,'ratings':ratings}
  # return render(request,'review.html',context)
  return render(request,'single_project.html',context)

class ProjectList(APIView):
  def get(self, request, format=None):
    all_projects = Project.objects.all()
    serializers = ProjectsSerializer(all_projects,many=True)
    return Response(serializers.data)
  
class RatingList(APIView):
  def get(self,request,format=None):
    all_ratings = Rating.objects.all()
    serializers = RatingSerializer(all_ratings,many=True)
    return Response(serializers.data)
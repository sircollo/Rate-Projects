from django.urls import path,include,re_path as url
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    url('^$', views.home, name='index'),
    url('^signup/', views.signup, name='signup'),
    url('^signin/', views.signin, name='signin'),
    url('logout/', SignOutView.as_view(), name='logout'),
    url('^profile/(\d+)', views.profile, name='profile'),
    path('update-profile/<str:id>/', views.updateProfile, name='update_profile'),
    url('^upload-project/(\d+)', views.uploadProject, name='upload'),
    path('search/', search_user.as_view(), name='search'),
    url('^api/profiles/', views.ProfileList.as_view(), name='api-profiles'),
    url(r'^api-token-auth/', obtain_auth_token),
    url('review/(\d+)', views.reviews, name='reviews'),
    url('^api/projects/', views.ProjectList.as_view(), name='api-projects'),
    url('^api/ratings/', views.RatingList.as_view(), name='ratings'),
    url('^api/project/(\d+)/', views.ProjectDetail.as_view(), name='details'),
    url('^api/profile/(\d+)/', views.ProfileDetails.as_view(), name='profiles'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
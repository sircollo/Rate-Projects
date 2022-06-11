from django.urls import path,include,re_path as url
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url('^$', views.home, name='index'),
    url('^signup/', views.signup, name='signup'),
    url('^signin/', views.signin, name='signin'),
    url('logout/', SignOutView.as_view(), name='logout'),
    url('^profile/(\d+)', views.profile, name='profile'),
    path('update-profile/<str:id>', views.updateProfile, name='update_profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
from django.urls import path,include,re_path as url
from . import views
from .views import *

urlpatterns = [
    url('^$', views.home, name='index'),
    url('^signup/', views.signup, name='signup'),
    url('^signin/', views.signin, name='signin'),
    url('logout/', SignOutView.as_view(), name='logout'),
]

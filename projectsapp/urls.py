from django.urls import path,include,re_path as url
from . import views

urlpatterns = [
    url('$', views.home, name='index')
]

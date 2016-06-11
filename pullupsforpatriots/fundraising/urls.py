from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^$', views.placeholder, name='index'),
    url(r'^ourgoal/$', views.placeholder, name='ourgoal'),
    url(r'^marines/$', views.placeholder, name='marines'),
    url(r'^marines/search/$', views.placeholder, name='marines'),
    url(r'^marines/all/$', views.placeholder, name='marines'),
    url(r'^marines/(?P<pk>[0-9]+)/$', views.placeholder, name='marines'),
    url(r'^sponsors/$', views.placeholder, name='sponsors'),
    url(r'^donors/$', views.placeholder, name='donors'),
    ]
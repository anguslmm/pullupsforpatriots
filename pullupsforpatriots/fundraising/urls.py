from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^$', views.placeholder, name='index'),
    url(r'^ourgoal/$', views.OurGoalView, name='ourgoal'),
    url(r'^marines/$', views.MarinesView, name='marines'),
    url(r'^marines/search/$', views.MarinesView, name='marines'),
    url(r'^marines/all/$', views.MarinesView, name='marines'),
    url(r'^marines/(?P<pk>[0-9]+)/$', views.MarinesView, name='marines'),
    url(r'^sponsors/$', views.SponsorsView, name='sponsors'),
    url(r'^donors/$', views.DonorsView, name='donors'),
    ]
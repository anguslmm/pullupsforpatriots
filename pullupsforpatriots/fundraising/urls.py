from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ourgoal/$', views.ourgoal, name='ourgoal'),
    url(r'^marines/$', views.MarineView, name='marines'),
    url(r'^marines/search/$', views.MarineView, name='marines-search'),
    url(r'^marines/all/$', views.MarineView, name='marines-all'),
    url(r'^marines/(?P<pk>[0-9]+)/$', views.MarineView.as_view(), name='marines-detail'),
    url(r'^sponsors/$', views.SponsorsView.as_view(), name='sponsors'),
    url(r'^donors/$', views.DonorsView.as_view(), name='donors'),
    ]
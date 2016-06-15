from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sponsors/$', views.SponsorsView.as_view(), name='sponsors'),
    url(r'^companyd/$', views.companyd, name='companyd'),
    url(r'^companyd/search/$', views.companyd, name='companyd-search'),
    url(r'^companyd/all/$', views.companyd, name='companyd-all'),
    url(r'^companyd/about/$', views.companyd, name='companyd-about'),
    url(r'^niocga/$', views.niocga, name='niocga'),
    url(r'^niocga/search/$', views.niocga, name='niocga-search'),
    url(r'^niocga/all/$', views.niocga, name='niocga-all'),
    url(r'^niocga/about/$', views.niocga, name='niocga-about'),
    ]
from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^viewall/(?P<command_id>[0-9]+)$', views.view_all, name="view_all"),
    url(r'^search', views.search, name='search'),
    url(r'^sponsors/$', views.sponsors, name='sponsors'),
    url(r'^companyd/$', views.companyd, name='companyd'),
    url(r'^donate/(?P<marine_id>[0-9]+)$', views.donate, name='donate'),
    url(r'^startdonation/(?P<marine_id>[0-9]+)$', views.donation_start, name='start_donation'),
    url(r'^donationconfirm', views.donation_confirm, name='donation_confirm'),
    url(r'^donationcongrats/(?P<donation_id>[0-9]+)$', views.donation_congrats, name='donation_congrats'),
    url(r'^pledgeconfirm', views.pledge_confirm, name='pledge_confirm'),
    url(r'^pledge/(?P<marine_id>[0-9]+)$', views.pledge, name='pledge'),
    url(r'^startpledge/(?P<marine_id>[0-9]+)$', views.pledge_start, name='start_pledge'),
    url(r'^pledgecongrats/(?P<pledge_id>[0-9]+)$', views.pledge_congrats, name='pledge_congrats'),
    url(r'^companyd/search/$', views.companyd, name='companyd-search'),
    url(r'^companyd/all/$', views.companyd, name='companyd-all'),
    url(r'^companyd/about/$', views.companyd, name='companyd-about'),
    url(r'^niocga/$', views.niocga, name='niocga'),
    url(r'^niocga/search/$', views.niocga, name='niocga-search'),
    url(r'^niocga/all/$', views.niocga, name='niocga-all'),
    url(r'^niocga/about/$', views.niocga, name='niocga-about'),
    url(r'^.+modern-business.css$', views.moderncss),
    url(r'^.+custom.css$', views.customcss),
    url(r'^.+font-awesome.min.css$', views.facss),
    ]
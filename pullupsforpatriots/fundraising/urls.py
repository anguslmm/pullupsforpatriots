from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^donations/ourgoal/$', 'views.placeholder', name='ourgoal'),
    url(r'^donations/marines/$', 'views.placeholder', name='marines'),
    url(r'^donations/marines/search/$', 'views.placeholder', name='marines'),
    url(r'^donations/marines/all/$', 'views.placeholder', name='marines'),
    url(r'^donations/marines/:id/$', 'views.placeholder', name='marines'),
    url(r'^donations/sponsors/$', 'views.placeholder', name='sponsors'),
    url(r'^donations/donors/$', 'views.placeholder', name='donors'),
    ]
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Marines, Sponsor

class IndexView(generic.ListView):
    template_name = 'template/index.html'
    
class OurGoalView(generic.ListView):
    template_name = 'template/ourgoal.html'
    
class MarinesView(generic.ListView):
    model = Marines
    template_name = 'template/marines.html'
    
class SponsorsView(generic.ListView):
    model = Sponsor
    template_name = 'template/sponsor.html'

class DonorsView(generic.ListView):
    template_name = 'template/donors.html'
    
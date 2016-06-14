from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Marines, Sponsor, Donation

class IndexView(generic.DetailView):
    template_name = 'template/index.html'
    
class OurGoalView(generic.DetailView):
    template_name = 'template/ourgoal.html'
    
class MarinesView(generic.DetailView):
    model = Marines
    template_name = 'template/marines.html'
    
class SponsorsView(generic.DetailView):
    model = Sponsor
    template_name = 'template/sponsor.html'

class DonorsView(generic.DetailView):
    model = Donation
    template_name = 'template/donors.html'
    

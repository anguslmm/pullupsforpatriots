from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Marine, Sponsor, Donation

def placeholder(request):
    return HttpResponse("This is a placeholder.")

class MarineView(generic.DetailView):
    model = Marine
    template = "marine.html"

class IndexView(generic.DetailView):
    template_name = 'template/index.html'
    
class OurGoalView(generic.DetailView):
    template_name = 'template/ourgoal.html'
    
class SponsorsView(generic.DetailView):
    model = Sponsor
    template_name = 'template/sponsor.html'

class DonorsView(generic.DetailView):
    model = Donation
    template_name = 'template/donors.html'
    

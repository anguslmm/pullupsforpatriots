from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

def placeholder(request, pk=0):
    return HttpResponse("Hello, world. This is a placeholder view."
    
class OurGoalView(generic.ListView):
    template_name = 'template/ourgoal.html'
    
class MarinesView(generic.DetailedView):
    template_name = 'template/marines.html'
    
class SponsorView(generic.ListView):
    template_name = 'template/sponsor.html'

class DonorsView(generic.ListView):
    template_name = 'template/donors.html'
    
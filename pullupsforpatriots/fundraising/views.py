from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Marine, Sponsor, Donation

def placeholder(request):
    return HttpResponse("This is a placeholder.")

class MarineView(generic.DetailView):
    model = Marine
    template = "marine.html"

def ourgoal(request):
    return render(request, 'fundraising/ourgoal.html')
    
def index(request):
    return render(request, 'fundraising/index.html')
    
    
class SponsorsView(generic.ListView):
    model = Sponsor
    template_name = 'sponsor_list.html'

class DonorsView(generic.ListView):
    model = Donation
    template_name = 'donations_list.html'
    

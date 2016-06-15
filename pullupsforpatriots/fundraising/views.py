from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Marine, Sponsor, Donation

def placeholder(request):
    return HttpResponse("This is a placeholder.")
    
def companyd(request):
    return render(request, 'fundraising/companyd.html')
    
def niocga(request):
    return render(request, 'fundraising/niocga.html')
    
def index(request):
    return render(request, 'fundraising/index.html')
    
class SponsorsView(generic.ListView):
    model = Sponsor
    template_name = 'sponsor_list.html'
    

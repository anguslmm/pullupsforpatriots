from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
    
class OurGoalView(generic.ListView):
    template_name = 'template/ourgoal.html'
    
class MarinesView(generic.ListView):
    template_name = 'template/marines.html'
    search_fileds = ['marine.id']
    fieldsets = [
        (None, {'fields': ['marine.id']}),
    ]
    
class SponsorsView(generic.ListView):
    template_name = 'template/sponsor.html'

class DonorsView(generic.ListView):
    template_name = 'template/donors.html'
    
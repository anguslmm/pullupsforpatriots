from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Marine

class MarineView(generic.DetailView):
    model = Marine
    template = "marine.html"

def placeholder(request, pk=0):
    return HttpResponse("Hello, world. This is a placeholder view.")
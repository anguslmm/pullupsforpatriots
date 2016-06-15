from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

def placeholder(request):
    return HttpResponse("Hello, world. This is a placeholder view.")
    
def contacts(request):
    return render(request, 'contacts.html')

def homepage(request):
    return render(request, 'homepage.html')


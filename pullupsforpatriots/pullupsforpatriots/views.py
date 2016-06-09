from django.shortcuts import render
from django.http import HttpResponse

def placeholder(request):
    return HttpResponse("Hello, world. This is a placeholder view.")
    
def homepage(request):
    return render(request, 'templates/homepage.html')
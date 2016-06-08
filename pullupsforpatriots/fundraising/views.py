from django.shortcuts import render
from django.http import HttpResponse

def placeholder(request, pk=0):
    return HttpResponse("Hello, world. This is a placeholder view.")
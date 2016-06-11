from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

def placeholder(request):
    return HttpResponse("Hello, world. This is a placeholder view.")
    
class ContactsView(generic.ListView):
    template_name = 'templates/contacts.html'
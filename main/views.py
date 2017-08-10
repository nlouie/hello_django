from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# django views are synonymous to a controller in the MVC framework

def home(request):
    return render(request, "main/home.html", {'message': 'hi whats up'})

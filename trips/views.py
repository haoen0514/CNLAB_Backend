from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<p>Hello World!</p>")
# Create your views here. 

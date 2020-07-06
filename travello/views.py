from django.shortcuts import render
from django.http import HttpResponse
from . models import destination

# Create your views here.
def index(request):
    dests = destination.objects.all()
    #.map( lambda x: x.save())

    return render(request,'index.html',{'dests' : dests})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def destinations(request):
    return render(request,'destinations.html')

def elements(request):
    return render(request,'elements.html')

def news(request):
    return render(request,'news.html')
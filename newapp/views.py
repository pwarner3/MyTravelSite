from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def indexPageView(request) :
    return render(request,'newapp/index.html')

def aboutPageView(request) :
    return render(request,'newapp/about.html')
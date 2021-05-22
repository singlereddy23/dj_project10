from django.http.request import HttpRequest
from django.shortcuts import render

# Create your views here.

def smaple1(request):
    return render(request,"sample.html")
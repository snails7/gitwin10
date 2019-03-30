# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Front's first page")

def login(request):
    return HttpResponse("Front login page")


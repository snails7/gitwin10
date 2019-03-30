from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def book(request):
    return HttpResponse('图书首页')


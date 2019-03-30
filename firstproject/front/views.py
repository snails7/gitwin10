# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    # ?username = xxx
    username = request.GET.get('username')
    if username:
        return HttpResponse('Front main page!!!')
    else:
        return redirect('/login/')


def login(request):
    return HttpResponse("Front login page")


# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
#from django.shortcuts import redirect, reverse
from django.template.loader import render_to_string


# def index(request):
    # ?username = xxx
#    username = request.GET.get('username')
#    if username:
#        return HttpResponse('Front main page!!!')
#    else:
#        return redirect(reverse('front:login'))


# def login(request):
#     return HttpResponse("Front login page")

#def index(request):
#    html = render_to_string("index.html")
#    return HttpResponse(html)

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
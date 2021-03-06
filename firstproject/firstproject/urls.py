"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.urls import path,include
#from book import views
#from django.http import HttpResponse
#
#def index(request):
#    return HttpResponse("Main Page")
#
#urlpatterns = [
#    path('admin/', admin.site.urls),
#    # path('', index),
#    path('book/', views.book),
#    # /book/detail/1/
#    path("book/detail/<book_id>/<category_id>/", views.book_detail),
#
#    path('book/author/', views.author_detail),
#
#    path('',include('front.urls')),
#    path('cms/', include('cms.urls')),
#]


from django.urls import path
#from front import views
from . import views


urlpatterns = [
    path('', views.index),
]
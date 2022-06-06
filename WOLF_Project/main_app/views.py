from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class Conservation(TemplateView):
    template_name = 'conservation.html'
    

class Yourstory(TemplateView):
    template_name = "yourstory.html"


from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Video, Pack

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class Conservation(TemplateView):
    template_name = 'conservation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["videos"] = Video.objects.all()
        return context

class Yourstory(TemplateView):
    template_name = "yourstory.html"

class Yellowstonewolves(TemplateView):
    template_name = "yellowstone_wolves.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["packs"] = Pack.objects.all()
        return context


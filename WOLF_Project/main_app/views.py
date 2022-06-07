from xml.etree.ElementInclude import DEFAULT_MAX_INCLUSION_DEPTH
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Video, Pack, Story
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["storys"] = Story.objects.all()
        return context

class Yellowstonewolves(TemplateView):
    template_name = "yellowstone_wolves.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["packs"] = Pack.objects.all()
        return context

class PackDetail(DetailView):
    template_name = "pack_detail.html"
    model = Pack

class YourstoryCreate(CreateView):
    model = Story
    fields = ['name', 'title', 'story', 'story_Img']
    template_name = 'yourstory_create.html'
    success_url = '/yourstory/'

class YourstoryUpdate(UpdateView):
    model = Story
    fields = ['name', 'title', 'story', 'story_Img']
    template_name = 'yourstory_update.html'
    success_url = '/yourstory/'

class YourstoryDelete(DeleteView):
    model = Story
    template_name = 'yourstory_delete_confirm.html'
    success_url = '/yourstory/'
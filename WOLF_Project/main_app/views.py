from xml.etree.ElementInclude import DEFAULT_MAX_INCLUSION_DEPTH
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Video, Pack, Story
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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

@method_decorator(login_required, name='dispatch')
class YourstoryCreate(CreateView):
    model = Story
    fields = ['name', 'title', 'story', 'story_Img']
    template_name = 'yourstory_create.html'
    success_url = '/yourstory/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(YourstoryCreate, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class YourstoryUpdate(UpdateView):
    model = Story
    fields = ['name', 'title', 'story', 'story_Img']
    template_name = 'yourstory_update.html'
    success_url = '/yourstory/'

@method_decorator(login_required, name='dispatch')
class YourstoryDelete(DeleteView):
    model = Story
    template_name = 'yourstory_delete_confirm.html'
    success_url = '/yourstory/'

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("yourstory")
        else:
            context = {"form": form}
            return render(request,"registration/signup.html", context)


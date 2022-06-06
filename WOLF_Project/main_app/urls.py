from django.urls import path
from . import views



urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('conservation/', views.Conservation.as_view(), name="conservation"),
    path('yellowstonewolves', views.Yellowstonewolves.as_view(), name="wolves"),
    path('yourstory/', views.Yourstory.as_view(), name="yourstory"),

]
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('conservation/', views.Conservation.as_view(), name="conservation"),
    path('yellowstonewolves', views.Yellowstonewolves.as_view(), name="wolves"),
    path('yourstory/', views.Yourstory.as_view(), name="yourstory"),
    path('pack/<int:pk>/', views.PackDetail.as_view(), name="pack_detail"),
    path('yourstory/new/', views.YourstoryCreate.as_view(), name="yourstory_create"),
    path('yourstory/<int:pk>/update', views.YourstoryUpdate.as_view(), name="yourstory_update"),
    
]


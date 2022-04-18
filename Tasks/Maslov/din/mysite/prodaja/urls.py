from re import template
from django.conf.urls import url, include
from django.views.generic import ListView,DetailView
from prodaja.models import Articles
from . import views


urlpatterns = [
    url(r'^price/$', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],
    template_name="prodaja/price.html")), 
    url(r'^login/$', views.user_login, name='login'),
    
]

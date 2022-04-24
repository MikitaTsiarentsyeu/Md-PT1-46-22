from re import template
from django.conf.urls import url, include
from django.views.generic import ListView,DetailView
from prodaja.models import Articles
from . import views 



urlpatterns = [
    url(r'^price/$', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],
 template_name="prodaja/price.html")), 
    # url(r'^price/$', views.price, name='price'),
   
    url(r'^register/$', views.register, name='register'),
    url(r'^register_done/$', views.register_done, name='register_done'),
    
    
]

   

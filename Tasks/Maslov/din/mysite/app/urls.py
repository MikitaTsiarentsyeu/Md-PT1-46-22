from django.conf.urls import url,include
from .import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^about/$', views.about, name='about'),
    
   
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.comments, name='comments'),
    path('add_review', views.add_review, name='add_review'),
]


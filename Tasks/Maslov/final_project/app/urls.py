from app.views import HomeView, ContactsView
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('contacts/', ContactsView.as_view()),
]
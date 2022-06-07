from datetime import date
from django.shortcuts import render
from .models import Services
from django.views.generic import DetailView


def services(request):
    service = Services.objects.order_by('service_name')
    return render(request, 'services/services.html', {'service': service})


class ServicesDetailView(DetailView):
    model = Services
    template_name = 'services/service_detail.html'
    context_object_name = 'service'

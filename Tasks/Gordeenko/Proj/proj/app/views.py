from django.shortcuts import render
from urllib import request
from datetime import datetime
from .forms import AddRequestModelForm
from .models import Tourist 
from django.shortcuts import redirect, render


# Create your views here.
def home(request):
    return render(request, 'home.html')

def home2(request):
    return render(request, 'home2.html')

def home3(request):
    return render(request, 'home3.html')

def home4(request):
    return render(request, 'home4.html')

def home5(request):
    return render(request, 'home5.html')

def requests(request):
    all_requests = Tourist.objects.all()
    return render(request, 'home5.html', {'requests':all_requests})

    
def add_request_model_form(request):

    if request.method == 'POST':
        form = AddRequestModelForm(request.POST)

        if form.is_valid():
            post = Tourist()
            post.title = form.cleaned_data['title']
            post.title = form.cleaned_data['name']
            post.title = form.cleaned_data['email']
            post.title = form.cleaned_data['phone']
            post.title = form.cleaned_data['convenient_time_to_call']
            post.title = form.cleaned_data['travel_type']
            post.title = form.cleaned_data['travel_services']
            post.title = form.cleaned_data['activities']
            post.title = form.cleaned_data['attractions']
            post.title = form.cleaned_data['comments']
            post.title = form.cleaned_data['sign_up_for_our_mailing_list']
            post.issued = datetime.now()

            post.save()

            return redirect('requests')
    else:
        form = AddRequestModelForm()

    return render(request, 'home3.html', {'form':form})





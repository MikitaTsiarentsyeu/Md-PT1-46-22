from django.shortcuts import render,redirect
from .forms import FeedbackForm
from .forms import CallBackForm
from django.contrib import messages
from .models import Feedback
# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def feedback(request):
    form = FeedbackForm
    if request.method=="POST":
        feedbackForm = FeedbackForm(request.POST)
        if feedbackForm.is_valid():
            feedbackForm.save()
            messages.success(request,"Thanks for the feedback!It's important for me!")
            return redirect('/feedback')
    return render(request,'feedback.html',{'form':form})



def viewfeedback(request):
    view = Feedback.objects.all()
    return render(request,"all_comments.html",{'view':view})


def callback(request):
    call = CallBackForm
    if request.method=="POST":
        callbackForm = CallBackForm(request.POST)
        if callbackForm.is_valid():
            callbackForm.save()
            messages.success(request,"Thank you! I'll contact with you soon!")
    return render(request,'home.html',{'call':call})

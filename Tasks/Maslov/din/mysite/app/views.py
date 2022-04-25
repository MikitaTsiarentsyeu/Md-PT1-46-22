from django.shortcuts import render



def home(request):
    return render(request, 'app/home.html')
def contacts(request):
    return render(request, 'app/contacts.html')
def about(request):
    return render(request, 'app/about_Us.html')




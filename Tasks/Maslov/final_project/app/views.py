from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
def contacts(request):
    return render(request, 'contacts.html')
def about(request):
    return render(request, 'about_Us.html')
def login(request):
    return render(request, 'login.html')
def price(request):
    return render(request, 'price.html')
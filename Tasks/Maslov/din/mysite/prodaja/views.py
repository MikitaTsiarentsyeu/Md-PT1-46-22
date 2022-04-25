
from .forms import  UserRegistrationForm
from .models import Product
from django.shortcuts import redirect, render



def price(request):
    return render(request, 'prodaja/price.html')

def all_product(request):
  

  all_product = Product.objects.all

  context = {
    'all_product': all_product,
  }

  return render(request, 'prodaja/price.html', context)
def register_done(request):
    return render(request, 'prodaja/register_done.html')
 
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
           
            new_user = user_form.save(commit=False)
        
            new_user.set_password(user_form.cleaned_data['password'])
            
            new_user.save()
            return render(request, 'prodaja/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'prodaja/register.html', {'user_form': user_form})
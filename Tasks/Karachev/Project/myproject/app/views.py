from datetime import datetime
from django.shortcuts import redirect, render
from .forms import AddReview
from .models import Review
from .models import Recipe
import random



def home(request):
    return render(request, 'home.html')

def reviews(request):
    all_reviews = Review.objects.all().order_by('-published')
    if request.method == 'POST':
        form=AddReview(request.POST)
        if form.is_valid():
            review = Review()
            review.person_name = form.cleaned_data['person_name']
            review.mail = form.cleaned_data['mail'] 
            review.content = form.cleaned_data['content']
            review.published = datetime.now()

            review.save()
        return redirect('reviews')
    else:
        form = AddReview()
    context_dict = { 'reviews' : all_reviews, 'form': form}    
    return render(request, 'reviews.html', context_dict)

def recipe(request):
    n_id = Recipe.objects.all().last().id 
    food_number= random.randint(1,n_id)
    recipe_id = Recipe.objects.get(id=food_number)
    return render(request, 'recipe.html', {'recipe':recipe_id} )



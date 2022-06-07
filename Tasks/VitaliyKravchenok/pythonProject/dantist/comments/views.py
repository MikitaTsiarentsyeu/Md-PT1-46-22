from django.shortcuts import render, redirect
from .models import Comments
from django.views.generic import DetailView
from .forms import AddReview
from datetime import datetime


def comments(request):
    comment = Comments.objects.order_by('-date')
    return render(request, 'comments/comments.html', {'comment': comment})


def add_review(request):
    if request.method == 'POST':
        form = AddReview(request.POST)
        if form.is_valid():
            review = Comments()
            review.author = form.cleaned_data['author']
            review.date = datetime.now()
            review.review_text = form.cleaned_data['review_text']
            review.author_email = form.cleaned_data['author_email']

            review.save()

        return redirect('comments')

    else:
        form = AddReview
    return render(request, 'comments/add_review.html', {'form': form})


#class ReviewDetailView(DetailView):
    #model = Comments
    #template_name = 'comments/review.html'
    #context_object_name = 'review'

from django import forms


class AddReview (forms.Form):
    author = forms.CharField(max_length=30, label='Name')
    author_email = forms.EmailField(label='Email')
    review_text = forms.CharField(widget=forms.Textarea, max_length=10000, label='Leave your review')


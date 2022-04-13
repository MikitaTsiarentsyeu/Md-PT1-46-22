from operator import imod
from django import forms

class AddReview(forms.Form):
    person_name = forms.CharField(max_length=50, label='Ваше имя')
    mail = forms.EmailField(label='Ваш email')
    content = forms.CharField(widget=forms.Textarea, label='Ваше мнение о нас')

    
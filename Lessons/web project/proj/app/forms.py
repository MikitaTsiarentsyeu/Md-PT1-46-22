from cProfile import label
from email import contentmanager
from random import choices
from turtle import title
from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class AddPost(forms.Form):

    title = forms.CharField(max_length=100, label='Title')
    subtitle = forms.CharField(max_length=200, label='Subtitle')
    content = forms.CharField(widget=forms.Textarea)
    post_type = forms.ChoiceField(choices=Post.POST_TYPES)
    image = forms.ImageField(label="Main image")

    def clean_subtitle(self):

        subtitle_data = self.cleaned_data['subtitle']
        title_data = self.cleaned_data['title']

        if subtitle_data == title_data:
            raise ValidationError("The title and subtitle should differ")

        return subtitle_data


class AddPostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'content', 'post_type', 'image')
        labels = {'image': 'hero image'}
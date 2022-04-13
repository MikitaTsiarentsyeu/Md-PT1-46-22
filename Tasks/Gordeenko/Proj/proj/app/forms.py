from django import forms
from .models import Tourist


class AddRequestModelForm(forms.ModelForm):
    class Meta:
        model = Tourist
        fields = ('title', 'name', 'email', 'phone', 'convenient_time_to_call', 'travel_type', 'travel_services', 'activities', 'attractions','attractions', 'comments', 'sign_up_for_our_mailing_list', 'issued')
        labels = {'email': 'E-mail'}


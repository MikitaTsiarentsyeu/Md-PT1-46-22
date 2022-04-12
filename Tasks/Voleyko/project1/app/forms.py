from django.forms import ModelForm
from .models import Feedback
from .models import CallBack

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields='__all__'

class CallBackForm(ModelForm):
    class Meta:
        model = CallBack
        fields = '__all__'
        
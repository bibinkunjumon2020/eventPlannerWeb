from django import forms
from django.contrib.auth.models import User
from apps.post.models import PostModel
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
class DateInput(forms.DateInput):
    input_type = 'date'


def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Future Events Only-Check Date")
class PostForm(forms.ModelForm):
    #event_date = forms.DateField(required=True,initial=datetime.date.today,validators=[validate_date],widget=forms.NumberInput(attrs={'type': 'date',"class": "form-control"}))
    class Meta:
        model = PostModel
        #exclude = ['user',]
        fields = ['event_title','event_date','content','location','pic']

        widgets={
            "event_date":forms.DateInput(attrs={'type':'date',}),
            "location":forms.TextInput(attrs={"class": "form-control", 'placeholder': 'event location','pattern':'[A-Z a-z . \']+','title':'Enter Characters Only'}),
            "event_title":forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Event tag name ?','pattern':'[A-Z a-z ! : # 0-9 . \']+','title':'Improper Input Symbol [A-Z a-z ! : # 0-9 . \']'}),
            "content":forms.Textarea(attrs={"class": "form-control",'placeholder':"Brief description about the event..."})
        }

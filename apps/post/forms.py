from django import forms
from django.contrib.auth.models import User
from apps.post.models import PostModel

class PostForm(forms.ModelForm):

    class Meta:
        model = PostModel
        exclude = ['user',]

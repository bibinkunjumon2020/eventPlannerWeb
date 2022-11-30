from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_title = models.CharField(max_length=120, null=False)
    event_date = models.DateField(null=False)
    content = models.TextField(null=False)
    location = models.CharField(max_length=200, null=False)
    date = models.DateField(auto_now_add=True)
    pic = models.ImageField(upload_to='events',
                            validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])], null=False,
                            blank=False)
    download_file = models.FileField(upload_to='event_pdf',blank=True,null=True)

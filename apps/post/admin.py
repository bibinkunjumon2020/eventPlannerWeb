from django.contrib import admin
from .models import *


# Register your models here.
class PostAdmin(admin.ModelAdmin):  # its our custom class in superuser to manage admin page
    fields = ["user", "event_title", "event_date", "content", "location", "date", "pic"]
    search_fields = ["event_title", "event_date", "location"]  # Where to be searched
    list_filter = ["event_date", "location"]  # filter shows these categores
    list_display = ["event_title", "event_date", "content", "location", "date", "pic"]  # it displays all these columns
    list_editable = ["event_date", "location"]  # what can edit after saved


admin.site.register(PostModel, PostAdmin)  # original model,new model

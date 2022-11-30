from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib import messages
from django.utils.decorators import method_decorator
from apps.post import forms
from apps.verified_access import login_required
from apps.post.models import PostModel
from django.http import FileResponse

from apps.task.task import generate_pdf


import zipfile
from io import BytesIO
from django.http import HttpResponse

# Post Views

@method_decorator(login_required, name="dispatch")
class MyAccountView(TemplateView):
    """
    View for loading the post_list html page
    """
    """User dashboard rendering class"""
    template_name = "eventWebsite/post_list.html"


class MyServicesView(TemplateView):
    """
    View for loading the services html page
    """
    template_name = "eventWebsite/services.html"


class MyContactView(TemplateView):
    """
    View for loading the contact html page
    """
    template_name = "eventWebsite/contact.html"


# Add New Post by a Logged-in user
@method_decorator(login_required, name="dispatch")
class PostCreateView(CreateView):
    """
    CreateView used to new post creation with form given data,depends on model
    """

    template_name = "eventWebsite/add_post.html"
    model = PostModel
    form_class = forms.PostForm
    success_url = "post_list"

    def form_valid(self, form):
        """
        Used to add instance value 'user' to the creation form
        """
        form.instance.user = self.request.user
        return super().form_valid(form)


# Listing Posts of a Logged-in user
@method_decorator(login_required, name="dispatch")
class ListPostView(ListView):
    """
    ListView used to list of posts with form given data,depends on model
    """
    template_name = "eventWebsite/post_list.html"
    model = PostModel
    context_object_name = 'posts'  # with this data can be accessed in front end html

    def get_queryset(self):
        """
        this specific query is used to run this View
        """
        return PostModel.objects.filter(user=self.request.user)

    def post(self,*args,**kwargs): # For using btn generate_pdf
        btn = self.request.POST.get('post_list_btn')
        if btn == 'generate_pdf':
            response = generate_pdf.delay()
            print("Task-Id.....", response)
            return redirect("post_list")
        return HttpResponse(status=400)
"""
class DownloadPostView(ListView):
   
    #ListView used to list of posts with form given data,depends on model
   
    template_name = "eventWebsite/post_list.html"
    model = PostModel
    context_object_name = 'posts'  # with this data can be accessed in front end html

    # queryset = PostModel.objects.all()
    # for element in queryset:
    #   print("???????????????//////////",element.id)

    # def get(self,*args,**kwargs):
    def get(self, *args, **kwargs):
        response = generate_pdf.delay()
        print("Task-Id.....", response)
        return super().get(self.request, *args, **kwargs)"""


# Listing all posts of all users in home page
class AllPostListView(ListView):
    template_name = "eventWebsite/home.html"
    model = PostModel
    context_object_name = "posts"  # with this data can be accessed in front end html

    def get_queryset(self):  # by default objects.all()  is the query.Only to override this fn
        """
        This query used which order the list in given value based
        """
        return PostModel.objects.all().order_by('event_date')

    # Delete Post


# class DeletePostView(DeleteView):  # but there is no sperate view for delete
#   template_name = "eventWebsite/post_list.html"
#   model = PostModel
#   success_url = reverse_lazy('post_list')


def delete_post(request, *args, **kwargs):  # path : /delete/<int:id>
    """
    It's a function for deleting list entries
    """
    PostModel.objects.get(id=kwargs.get('pk')).delete()
    messages.success(request, "Successfully Deleted an Event")
    return redirect("post_list")


class PostDetailView(DetailView):
    """
    DetailView used to show the detail of a specific post
    """
    template_name = "eventWebsite/post_detail.html"
    model = PostModel
    context_object_name = "post"  # with this data can be accessed in front end html


@method_decorator(login_required, name="dispatch")
class PostUpdateView(UpdateView):
    """
    UpdateView used to update the detail of a specific post
    """

    model = PostModel
    template_name = "eventWebsite/add_post.html"
    form_class = forms.PostForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        messages.success(self.request, "Post Updated")
        return super().form_valid(form)  # It helps to load existing value to the form


""" here pdf generated using another method..so dont delete
def generate_pdf(request, *args, **kwargs):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    data = PostModel.objects.filter(id=kwargs.get('pk')).values('event_title', 'event_date', 'content', 'location')[0]
    print(data)
    p.drawString(260, 800, "POST DETAIL PRINT")
    p.line(5, 780, 590, 780)  # drawing a line starting and ending coordinates given (0 to 600 is width A4 paper)
    x1 = 20
    y1 = 750
    for key, val in data.items():
        p.drawString(x1, y1, f"{key}   -  {val}")
        y1 = y1 - 60
    p.showPage()
    p.save()
    # p.setTitle(data.get('event_title'))
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=data.get('event_title'))"""




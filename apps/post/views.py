from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib import messages
from django.utils.decorators import method_decorator
from apps.post import forms
from apps.verified_access import login_required
import logging
from apps.post.models import PostModel

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
class ListPostView(ListView):
    """
    ListView used to list of posts with form given data,depends on model
    """
    template_name = "eventWebsite/post_list.html"
    model = PostModel
    context_object_name = 'posts' # with this data can be accessed in front end html

    def get_queryset(self):
        """
        this specific query is used to run this View
        """
        return PostModel.objects.filter(user=self.request.user)

# Listing all posts of all users in home page
class AllPostListView(ListView):
    template_name = "eventWebsite/home.html"
    model = PostModel
    context_object_name = "posts" # with this data can be accessed in front end html

    def get_queryset(self):  # by default objects.all()  is the query.Only to override this fn
        """
        This query used which order the list in given value based
        """
        return PostModel.objects.all().order_by('event_date')

    # Delete Post


# class DeletePostView(DeleteView):
#   template_name = "eventWebsite/post_list.html"
#  success_url = 'post_list'
# def get_queryset(self):
#    print("pk=",self.kwargs.get('pk'))
#   id=self.kwargs.get('pk')
#  return PostModel.objects.get(id=id).delete()


def delete_post(request, *args, **kwargs):  # path : todos/delete/<int:id>
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
    context_object_name = "post" # with this data can be accessed in front end html


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
        return super().form_valid(form) # It helps to load existing value to the form


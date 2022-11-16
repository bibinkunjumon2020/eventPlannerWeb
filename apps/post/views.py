from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib import messages
from django.utils.decorators import method_decorator
from apps.post import forms
from apps.verified_access import login_required
import logging
from apps.post.models import PostModel


# Create your views here.
@method_decorator(login_required, name="dispatch")
class MyAccountView(TemplateView):
    """User dashboard rendering class"""
    template_name = "eventWebsite/post_list.html"
class MyServicesView(TemplateView):
    """User dashboard rendering class"""
    template_name = "eventWebsite/services.html"
class MyContactView(TemplateView):
    """User dashboard rendering class"""
    template_name = "eventWebsite/contact.html"


# Adding posts by a specific user
class PostCreateView(CreateView):
    # Add Post
    template_name = "eventWebsite/add_post.html"
    model = PostModel
    form_class = forms.PostForm
    success_url = "post_list"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Listing Posts of a specific User
class ListPostView(ListView):
    template_name = "eventWebsite/post_list.html"
    model = PostModel
    context_object_name = 'posts'

    def get_queryset(self):
        return PostModel.objects.filter(user=self.request.user)


class AllPostListView(ListView):
    template_name = "eventWebsite/home.html"
    model = PostModel
    context_object_name = "posts"

    def get_queryset(self):  # by default objects.all()  is the query.Only to override this fn
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
    PostModel.objects.get(id=kwargs.get('pk')).delete()
    messages.success(request, "Successfully Deleted an Event")
    return redirect("post_list")


class PostDetailView(DetailView):
    template_name = "eventWebsite/post_detail.html"
    model = PostModel
    context_object_name = "post"


class PostUpdateView(UpdateView):
    model = PostModel
    template_name = "eventWebsite/add_post.html"
    form_class = forms.PostForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        messages.success(self.request, "Success Edited")
        return super().form_valid(form)

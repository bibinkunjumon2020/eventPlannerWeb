from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from apps.user import forms
from apps.verified_access import login_required
import logging


# Create your views here.
class HomeView(TemplateView):
    """
        Loading the first page in our website.Used Template view
        """
    template_name = "eventWebsite/home.html"


class AboutUsView(TemplateView):
    """
    Loading the Abouts US HTMl page.Used Template view
    """
    template_name = "eventWebsite/about_us.html"


class RegistrationView(View):
    """ Method for accepting user credentials and creating a User
        Django inbuilt User Model is used.
    """

    def get(self, request, *args, **kwargs):
        """
        Rendering form fields
        """
        form = forms.RegistrationForm()
        return render(request, "eventWebsite/registration.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        """
        Saving the form data in Database.
        """
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            print("Registration Success")
            messages.success(self.request, "Registered as a User")
            return redirect('login')  # Success redirected to Login View
        else:
            print("Form Error")
            messages.error(self.request, "Error in Registration")
            return render(request, "eventWebsite/registration.html", context={"form": form})


class LogInView(View):

    """ User can log in with username and password.It uses built authenticate function """

    def get(self, request, *args, **kwargs):
        """
                Rendering form fields
                """
        form = forms.LoginForm()
        return render(request, "eventWebsite/login.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        """
            Use input credentials for authenticating
                """
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            logging.info("Username & Password", username, password)
            # print(username, password)
            user = authenticate(request, username=username, password=password) # inbuilt func
            logging.info("User", user)
            # print(user)
            if user is not None:
                # print("Authenticated Successfully")
                logging.info("Authenticated Successfully")
                login(request, user)
                messages.success(request, "Welcome to your Dashboard")
                return redirect('post_list')
            else:
                logging.error("No Such User")
                messages.error(request, "No such User")
                return redirect("register")

        else:
            logging.error("Form Error")
            messages.error(request, "Error in Form")
            return render(request, "eventWebsite/login.html", context={"form": form})

        return render(request, "eventWebsite/login.html", {"form": form})


@method_decorator(login_required, name="dispatch")
class LogOutView(View):
    """User logout class """

    def get(self, request, *args, **kwargs):
        logout(request)  # inbuilt func
        return redirect("home")

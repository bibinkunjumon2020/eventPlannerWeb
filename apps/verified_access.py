from django.shortcuts import redirect
from django.contrib import messages


def login_required(fn):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Login to Access")
            return redirect("login")
        else:
            return fn(request, *args, **kwargs)
    return wrapper

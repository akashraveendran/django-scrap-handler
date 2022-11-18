from django.http import HttpResponse
from django.shortcuts import redirect


def user_only(view_func):

    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('signin')

    return wrapper_function

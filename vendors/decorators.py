from django.shortcuts import redirect


def vendor_only(view_func):

    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'users':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('home')

    return wrapper_function


def not_auth_vendor(view_func):

    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'users':
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_function

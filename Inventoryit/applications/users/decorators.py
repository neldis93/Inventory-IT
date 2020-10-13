from django.http import  HttpResponse
from django.urls import reverse
from django.shortcuts import redirect

#from django.contrib.auth import authenticate

#from django import forms

def user_decorator(user_view):
    def wrap_func(request, *args, **kwargs):
        if not request.user.is_active:
            return redirect('users_app:login_user')
        # otra forma pero igual  
        #if request.user.is_anonymous:
            #return redirect('users_app:login_user')
        return user_view(request, *args, **kwargs)
    return wrap_func


# def user_decorator_login(user_view):
#     def wrapped_func(request, *args, **kwargs):
#         username= request.POST['username']
#         password= request.POST['password']
#         log= authenticate(username=username, password=password)

#         if not log:
#             raise forms.ValidationError('User data is not correct')  

#         return user_view(request, *args, **kwargs)
#     return wrapped_func 



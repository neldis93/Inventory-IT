from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import CreateView, View
from django.views.generic.edit import FormView

from .forms import RegisterForm, LoginForm
from .models import User
#from .decorators import user_decorator_login


class RegisterUserView(FormView):
    template_name= 'users/register.html'
    form_class=RegisterForm
    success_url= reverse_lazy('users_app:login_user')

    def form_valid(self, form):

        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            # **extrafields
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            phone=form.cleaned_data['phone'],

        )

        return super(RegisterUserView,self).form_valid(form)


class LoginUserView(FormView):
    template_name='users/login.html'
    form_class=LoginForm
    success_url= reverse_lazy('inventory_app:panel_admin')

    def form_valid(self,form):
        user= authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        #hacer el login
        login(self.request,user)
        return super(LoginUserView,self).form_valid(form)
        

    # @method_decorator(user_decorator_login)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(LoginUserView, self).dispatch(request, *args, **kwargs)


class LogoutUserView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse('users_app:login_user')
        )


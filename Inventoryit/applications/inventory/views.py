from django.shortcuts import render

from rest_framework.generics import ListAPIView
#
from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView

from django.http.response import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 
#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator

from .models import Inventory, ChangeControl
#from applications.users.decorators import user_decorator
from .forms import InventoryRegisterForm

from .serializers import SearchSerializer

"""
# este mixin requerira que el usuario este activo es decir logueado
class loginMixin(object):
    # sobreescribir el metodo get se encarga de gestionar la respuesta(response) a una peticion get
    # sobreescribir el metodo dispatch permite controlar la peticion(request)
    def dispatch(self,request, *args, **kwargs):
        if not request.user.is_active:
            #messages.error(request,'no tiene permiso para entrar en este panel')
            return HttpResponseRedirect(reverse('users_app:login_user'))

        return super(loginMixin, self).dispatch(request, *args, **kwargs)
"""



#@method_decorator(login_required(login_url=reverse_lazy('users_app:login_user')),name='dispatch')  
class PanelHomeView(LoginRequiredMixin,TemplateView):
    template_name='panel.html'
    login_url= reverse_lazy('users_app:login_user')

    # @method_decorator(user_decorator)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(PanelHomeView, self).dispatch(request, *args, **kwargs)


class ListInventoryView(LoginRequiredMixin,ListView):
    template_name='inventory/list.html'
    model= Inventory
    context_object_name='list_inventory'
    #paginate_by=2
    login_url= reverse_lazy('users_app:login_user')
    
    def get_queryset(self):
        keyword= self.request.GET.get('keyword','')
        acronym= self.request.GET.get('acronym','')
        list_inv= Inventory.objects.list_all_filter(keyword, acronym)
        return list_inv
        

# tambien puedo hacerlo con un CreateView    
class RegisterInventoryView(LoginRequiredMixin,FormView):
    template_name='inventory/regis_inventory.html'
    form_class= InventoryRegisterForm
    success_url= reverse_lazy('inventory_app:panel_admin')
    login_url= reverse_lazy('users_app:login_user')
    
    def form_valid(self, form):
        # Guardado de datos en la DB
        inventory= form.save()

        return super(RegisterInventoryView, self).form_valid(form)
        

class InventoryUpdateView(LoginRequiredMixin,UpdateView):
    template_name='inventory/update_inventory.html'
    model= Inventory
    fields=('__all__')

    success_url= reverse_lazy('inventory_app:panel_list')
    login_url= reverse_lazy('users_app:login_user')

    def post(self, request, *args, **kwargs):
        self.object= self.get_object()

        return super(InventoryUpdateView, self).post(request,*args,**kwargs)

    
class InventoryDeleteView(LoginRequiredMixin,DeleteView):
    template_name='inventory/delete_inventory.html'
    model= Inventory
    success_url= reverse_lazy('inventory_app:panel_list')
    login_url= reverse_lazy('users_app:login_user')


"""Here start services"""
 
class InventoryListApiView(ListAPIView):
    serializer_class= SearchSerializer

    def get_queryset(self):
        # asi se recupera en los servicios rest 
        kword= self.request.query_params.get('kword','')
        
        return Inventory.objects.filter(
            nuuma__icontains=kword
            )


"""Change control"""

class ChangeControlView(LoginRequiredMixin,ListView):
    template_name= 'inventory/change_control.html'
    model= ChangeControl
    context_object_name='list_change_control'

    def get_queryset(self):
        keyword= self.request.GET.get('keyword','')

        return ChangeControl.objects.filter(
            ticket__icontains=keyword
            )


class ChangeControlRegisterView(LoginRequiredMixin, CreateView):
    template_name='inventory/register_control.html'
    model= ChangeControl
    fields=('__all__')
    success_url= reverse_lazy('inventory_app:control_list')
    login_url= reverse_lazy('users_app:login_user')

    def form_valid(self, form):
        # Guardado de datos en la DB
        change_control= form.save()

        return super(ChangeControlRegisterView, self).form_valid(form)


class ChangeControlUpdateView(LoginRequiredMixin,UpdateView):
    template_name='inventory/update_control.html'
    model= ChangeControl
    fields=('__all__')   
    success_url= reverse_lazy('inventory_app:control_list')
    login_url= reverse_lazy('users_app:login_user')

    # con este metodo hago un guardado de los datos 
    def post(self, request, *args, **kwargs):
        self.object= self.get_object()
        return super(ChangeControlUpdateView, self).post(request, *args, **kwargs)


class ChangeControlDeleteView(LoginRequiredMixin, DeleteView):
    template_name='inventory/delete_control.html'
    model= ChangeControl
    success_url= reverse_lazy('inventory_app:control_list')
    login_url= reverse_lazy('users_app:login_user')
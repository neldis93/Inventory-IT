from django.shortcuts import render

from django.views.generic import View, TemplateView, ListView, CreateView
from django.views.generic.edit import FormView

from django.http.response import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
#from django.contrib.auth.mixins import LoginRequiredMixin 
#from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


#from .forms import InventoryForm
from .models import Inventory
from applications.users.decorators import user_decorator
from .forms import InventoryRegisterForm


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
class PanelHomeView(TemplateView):
    template_name='panel.html'
    #login_url= reverse_lazy('users_app:login_user')

    @method_decorator(user_decorator)
    def dispatch(self, request, *args, **kwargs):
        return super(PanelHomeView, self).dispatch(request, *args, **kwargs)


class ListInventoryView(ListView):
    template_name='inventory/spain.html'
    #model= Inventory
    context_object_name='list_inventory'
    #paginate_by=2

    def get_queryset(self):
        #key_word= self.request.GET.get('kword','')
        #list_keyword= Inventory.objects.filter(hostname__icontains=key_word)
        
        return Inventory.objects.all()

    
class RegisterInventoryView(FormView):
    template_name='inventory/regis_inventory.html'
    form_class= InventoryRegisterForm
    success_url= reverse_lazy('inventory_app:panel_admin')
    
    def form_valid(self, form):

        inventory= form.save()

        return super(RegisterInventoryView, self).form_valid(form)
        
from django.urls import path

from . import views

app_name= 'inventory_app'

urlpatterns = [
    path('panel/',views.PanelHomeView.as_view(),name='panel_admin'),
    path('panel-spain/',views.ListInventoryView.as_view(),name='panel_spain'),
    path('register-inventory/',views.RegisterInventoryView.as_view(),name='panel_inventory'),
]
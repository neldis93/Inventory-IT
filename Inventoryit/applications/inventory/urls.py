from django.urls import path

from . import views

app_name= 'inventory_app'

urlpatterns = [
    path('panel/',views.PanelHomeView.as_view(),name='panel_admin'),
    path('panel-list/',views.ListInventoryView.as_view(),name='panel_list'),
    path('register-inventory/',views.RegisterInventoryView.as_view(),name='register_inventory'),
    path('update-inventory/<pk>/',views.InventoryUpdateView.as_view(),name='update_inventory'),
    path('delete-inventory/<pk>/',views.InventoryDeleteView.as_view(),name='delete_inventory'),
    path('change-control/',views.ChangeControlView.as_view(),name='control_list'),
    path('register-control/',views.ChangeControlRegisterView.as_view(),name='control_register'),
    path('update-control/<pk>/',views.ChangeControlUpdateView.as_view(),name='control_update'),
    path('delete-control/<pk>/',views.ChangeControlDeleteView.as_view(),name='control_delete'),
    #url de servicios
    path('api/search/list/',views.InventoryListApiView.as_view(), name='list_search')
]
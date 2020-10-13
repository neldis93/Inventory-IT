from django import forms

from .models import Inventory

class InventoryRegisterForm(forms.ModelForm):

    class Meta:
        model= Inventory
        fields=(
            'location',
            'direction',
            'hostname',
            'nuuma',
            'serial_number',
            'product_number',
            'mac_address',
            'mac_wifi',
            'manufacturer',
            'name',
            'model',
        )
        widgets= {
            'location':forms.TextInput(attrs={'placeholder':'Location', 'class':'form-control',}),
            'direction': forms.TextInput(attrs={'placeholder':'Direction', 'class':'form-control',})


        }
        
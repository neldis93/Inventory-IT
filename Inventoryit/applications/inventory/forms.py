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
            'observations',
            'warranty',
        )
        widgets= {
            'location':forms.TextInput(
                attrs={
                    'placeholder':'...', 
                    'class':'form-control',
                }
            ),
            'direction': forms.TextInput(
                attrs={
                    'placeholder':'...', 
                    'class':'form-control',
                }
            ),
            'hostname': forms.TextInput(
                attrs={
                    'placeholder':'...', 
                    'class':'form-control',
                }
            ),
            'nuuma':forms.TextInput(
                attrs={
                    'placeholder':'...', 
                    'class':'form-control',
                }
            ),
            'serial_number':forms.TextInput(
                attrs={
                    'placeholder':'...', 
                    'class':'form-control',
                }
            ),
            'product_number': forms.TextInput(
                attrs={
                    'placeholder':'...', 
                    'class':'form-control',
                }
            ),
            'mac_address': forms.TextInput(
                attrs={
                    'placeholder':'...', 
                    'class':'form-control',
                }
            ),
            'mac_wifi': forms.TextInput(
                attrs={
                    'placeholder':'...', 
                    'class':'form-control',
                }
            ),
            'manufacturer': forms.TextInput(
                attrs={
                    'placeholder':'...', 
                    'class':'form-control',
                }
            ),

            'name': forms.TextInput(
                attrs={
                    'placeholder':'...', 
                    'class':'form-control',
                }
            ),
             'observations': forms.TextInput(
                attrs={
                    'placeholder':'...', 
                    'class':'form-control',
                }
            ),
            'warranty': forms.TextInput(
                attrs={
                    'placeholder':'...', 
                    'class':'form-control',
                }
            ),
        }
        

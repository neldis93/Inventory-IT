#import re
from django import forms
from django.contrib.auth import authenticate


from .models import User

class RegisterForm(forms.ModelForm):

    password1= forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password',
                    'class':'form-control'
            }
        )
    )
    
    password2= forms.CharField(
        label=' Repeat password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repeat password',
                'class':'form-control'
            }
        )
    )

    class Meta:
        model= User
        fields= (
            'username',
            'email',
            'first_name',
            'last_name',
            'phone',
            )
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                    'class': 'form-control',
                    
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                    'class': 'form-control',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First name',
                    'class': 'form-control',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last name',
                    'class': 'form-control',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Phone',
                    'class': 'form-control',
                },
            ),

        }
      
    # validar la contraseña para verificar que sean las mismas cuando ingrese el password1 y password2
    def clean_password2(self):

        #password1= self.cleaned_data['password1']
        #password2= self.cleaned_data['password2']

        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            # el add_error vincula el error al campa se le indica, en este caso password2
            self.add_error('password2', 'Passwords are not the same') # tambien se puede utilizar el raise

    """
        #if len(self.cleaned_data['password1']) < '5' and len(self.cleaned_data['password1'] > '12':
            #raise forms.ValidationError('La contraseña debe ser mayor a 5 digitos y menor a 12')
        if not re.search('[a-z]', password1) and re.search('[A-Z]',password1):
            raise forms.ValidationError('Should contain mayoscules and minisculates')
        if not re.search('[_@#$%\/.,*+-]',password1):
            raise forms.ValidationError('Should contain special caracters')
                
        #if self.cleaned_data['password1'] < '5' and self.cleaned_data['password1'] > '12':
            #self.add_error('password1', 'La contraseña debe ser mayor a 5 digitos y menor a 12')
        
        


    def clean_email(self):
        email= self.cleaned_data.get('email')
        email_base, proveeder= email.split('@')
        dominio, extension = proveeder.split('.')

        if not 'mapfre' in email:
            raise forms.ValidationError('Please use an extension in the email. Mapfre')
        return email
"""

class LoginForm(forms.Form):

    username= forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Username',
                'class':'form-control'
            }
        )
    )
    
   
    password= forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password',
                'class':'form-control'
            }
        )
    )


# validar si un usuario existe o no en la base de datos y si sus datos estan correctos  
    def clean(self):
        # cleaned_data quiere decir que retorne todos los datos
        cleaned_data=super(LoginForm, self).clean()
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')

        if not authenticate(username=username,password=password):
            #self.add_error('username','User data is not correct')
            #self.add_error('password','Password is not correct')
            raise forms.ValidationError('Username OR password is incorrect')

        return self.cleaned_data


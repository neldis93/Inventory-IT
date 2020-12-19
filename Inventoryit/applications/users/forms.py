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
      
    def clean_password2(self):

        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Passwords are not the same') 

            
    #def clean_email(self):
        #email= self.cleaned_data.get('email')
        #email_base, proveeder= email.split('@')
        #dominion, extension = proveeder.split('.')

        #if not 'XXXX' in email:
            #raise forms.ValidationError('Please use an extension in the email XXXX')
        #return email
    

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
        cleaned_data=super(LoginForm, self).clean()
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')

        if not authenticate(username=username,password=password):
            #self.add_error('username','User data is not correct')
            #self.add_error('password','Password is not correct')
            raise forms.ValidationError('Username OR password is incorrect')

        return self.cleaned_data


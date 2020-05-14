from django.forms import ModelForm, widgets
from django import forms
from user.models import User

class UserCreateForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id']
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'register-input'}),
            'name': widgets.TextInput(attrs={'class': 'register-input'}),
            'address': widgets.TextInput(attrs={'class': 'register-input'}),
            'email': widgets.EmailInput(attrs={'class': 'register-input'}),
            'phoneno': widgets.TextInput(attrs={'class': 'register-input'})
        }
    password = forms.CharField(required=True, label="Password",
                                 widget=forms.PasswordInput(attrs={'class': 'register-input'})
                                 )

class UserLoginPage(ModelForm):
    class Meta:
        model = User
        exclude = ['id']
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'form-control'}),
            'password': widgets.TextInput(attrs={'class': 'form-control'})
        }

#'password': widgets.PasswordInput(attrs={'class': 'form-control'})
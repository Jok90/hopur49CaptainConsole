from django.forms import ModelForm, widgets
from django import forms
from user.models import User

class UserCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        exclude = ['id']
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'form-control'}),
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
            'phoneno': widgets.TextInput(attrs={'class': 'form-control'})
        }
    password = forms.CharField(required=True, label="Password",
                                 widget=forms.PasswordInput(attrs={'class': 'form-control'})
                                 )

class UserLoginPage(ModelForm):
    class Meta:
        model = User
        exclude = ['id']
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'form-control'}),
            'password': widgets.TextInput(attrs={'class': 'form-control'})
        }


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id']
        widgets = {
            'username'
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'phoneno': widgets.NumberInput(attrs={'class': 'form-control'}),

        }

#'password': widgets.PasswordInput(attrs={'class': 'form-control'})
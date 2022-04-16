from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from .models import NewUser


class Person(ModelForm):

    class Meta:

        model = NewUser
        fields = ["username", "email", "first_name", "middle_name", "last_name",
                  "gender", "country", "password"]

        labels = {
            'username': "",
            'email': "",
            'first_name': "",
            'middle_name': "",
            'last_name': "",
            'gender': "",
            'country': "",
            'password': "",
        }

        widgets = {
            'username': TextInput(attrs={
                'readonly onfocus': 'this.removeAttribute (\'readonly\');',
                'class': 'Username',
                'id': 'username',
                'name': 'username',
                'placeholder': 'Username',
            }),
            'email': EmailInput(attrs={
                'readonly onfocus': 'this.removeAttribute (\'readonly\');',
                'class': 'Email',
                'id': 'email',
                'name': 'email',
                'placeholder': 'Email',
            }),
            'first_name': TextInput(attrs={
                'readonly onfocus': 'this.removeAttribute (\'readonly\');',
                'class': 'First_Name',
                'id': 'first_name',
                'name': 'first_name',
                'placeholder': 'First_Name',
            }),
            'middle_name': TextInput(attrs={
                'readonly onfocus': 'this.removeAttribute (\'readonly\');',
                'class': 'Middle_Name',
                'id': 'middle_name',
                'name': 'middle_name',
                'placeholder': 'Middle Name',
            }),
            'last_name': TextInput(attrs={
                'readonly onfocus': 'this.removeAttribute (\'readonly\');',
                'class': 'Last_Name',
                'id': 'last_name',
                'name': 'last_name',
                'placeholder': 'Last Name',
            }),
            'password': PasswordInput(attrs={
                'readonly onfocus': 'this.removeAttribute (\'readonly\');',
                'class': 'Password',
                'id': 'password',
                'name': 'password',
                'placeholder': 'Password',
            }),
        }


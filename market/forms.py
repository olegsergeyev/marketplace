from django import forms

from .models import Item

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('item_name', 'department', 'text', 'price', 'email',)

class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

class AuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password',)

import re

from django import forms

from .models import Item
from .models import User_r

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('item_name', 'department', 'text', 'price', 'email',)

class RegForm(forms.ModelForm):
    class Meta:
        model = User_r
        fields = ('username', 'name', 'email', 'password',)

    def clean_username(self):
        data = self.cleaned_data['username']
        pattern = re.compile(r'[^a-zA-Z0-9]+$')
        if pattern.search(data):
            raise forms.ValidationError("Используйте только символы A-Z, a-z, 0-9")
        return data

from django import forms
from market.models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('item_name', 'department', 'text', 'price', 'email',)

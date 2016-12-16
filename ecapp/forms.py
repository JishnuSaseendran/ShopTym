from django.contrib.auth.models import User
from django import forms
from .models import Item

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('item_name', 'item_cost', 'item_details','item_logo')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

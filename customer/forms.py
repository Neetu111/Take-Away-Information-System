from django import forms
from .models import Menu, Food, Drink, Order

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('MID', 'Price', )

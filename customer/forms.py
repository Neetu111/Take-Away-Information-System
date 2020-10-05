from django import forms
from .models import Menu, Food, Drink, Order, Person

class LoginForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Person
        fields = ('PID', 'First_Name', 'Last_Name', 'Password', 'Country', 'City', 'Email', 'Contact_Number', )

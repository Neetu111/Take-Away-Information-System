from django.shortcuts import render
from .models import Menu, Food, Drink, Order
from .forms import MenuForm

# Create your views here.

def customer_list(request):
    return render(request, 'customer/customer_list.html', {})


def menu_list(request):
    menus = Menu.objects.all()
    foods = Food.objects.all()
    drinks = Drink.objects.all()
    return render(request, 'customer/menu_list.html', {'menus' : menus, 'foods' : foods, 'drinks' : drinks })


# Useful for adding order option
# def menu_list(request):
#     forms = MenuForm
#     return render(request, 'customer/menu_list.html', {'forms' : forms})
# <a href="{% url 'menu_list' %}" class="top-menu">here</a>

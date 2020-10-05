from django.shortcuts import render
from .models import Menu, Food, Drink, Order
from .forms import LoginForm

# Create your views here.

def customer_list(request):
    return render(request, 'customer/customer_list.html', {})


def menu_list(request):
    menus = Menu.objects.values()
    foods = Food.objects.all()
    drinks = Drink.objects.all()
    context = {'menus' : menus, 'foods' : foods, 'drinks' : drinks }
    return render(request, 'customer/menu_list.html', context )


def customer_login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form':form}
    return render(request, 'customer/customer_login.html', context)

def order(request):
    menus = Menu.objects.values()
    foods = Food.objects.all()
    drinks = Drink.objects.all()
    context = {'menus' : menus, 'foods' : foods, 'drinks' : drinks }
    return render(request, 'customer/order.html', context )

def place_order(request):
    food_ID = request.POST.get('food_ID')
    context = {'food_ID' : food_ID}
    return render(request, 'customer/place_order.html', context )


# Useful for adding order option
# def menu_list(request):
#     forms = MenuForm
#     return render(request, 'customer/menu_list.html', {'forms' : forms})
# <a href="{% url 'menu_list' %}" class="top-menu">here</a>

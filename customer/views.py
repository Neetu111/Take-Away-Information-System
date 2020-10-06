from django.shortcuts import render
from .models import *
from .forms import LoginForm
import pandas as pd
import numpy as np
from itertools import chain
from operator import attrgetter
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

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
    previous_change = []
    error_msg = ""
    food_ID = request.POST.get('food_ID')[0:2]
    Orders = Order.objects.all()
    Own_Foods = Create_Your_Own_Food.objects.all()
    Customization = Customize.objects.values()
    test1 = Order.objects.values()

    stop_words = set(stopwords.words('english'))
    more_words = ['Add', 'add']
    new_stop_words = stop_words.union(more_words)
    test = Customize.objects.values_list('Changes', 'MID')
    custom_chnages = {}
    for x in test:
        cust_tokens = word_tokenize(x[0])
        filtered_cust = [filtered for filtered in cust_tokens if not filtered in new_stop_words ]
        custom_chnages[x[1]] = filtered_cust
    # print(custom_chnages)

    if food_ID in custom_chnages:
        previous_change = custom_chnages[food_ID]
    else:
        error_msg = "No Changes exist for this."

    context = {'food_ID' : food_ID, 'previous_change' : previous_change, 'error_msg': error_msg}
    return render(request, 'customer/place_order.html', context )


# Useful for adding order option
# def menu_list(request):
#     forms = MenuForm
#     return render(request, 'customer/menu_list.html', {'forms' : forms})
# <a href="{% url 'menu_list' %}" class="top-menu">here</a>

from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('menu', views.menu_list, name='menu_list'),
    path('login', views.customer_login, name = "customer_login"),
    path('order', views.order, name = "order"),
    path('place_order', views.place_order, name = "place_order")
]

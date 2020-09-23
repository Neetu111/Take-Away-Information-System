from django.contrib import admin

from .models import Person, Customer, Business_Owner, Menu

admin.site.register(Person)
admin.site.register(Customer)
admin.site.register(Business_Owner)
admin.site.register(Menu)

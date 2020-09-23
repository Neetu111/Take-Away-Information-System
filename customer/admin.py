from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *

admin.site.register(Person)
admin.site.register(Customer)
admin.site.register(Business_Owner)
admin.site.register(Menu)
admin.site.register(Food)
admin.site.register(Drink)

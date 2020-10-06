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
admin.site.register(Order)
admin.site.register(Order_Feedback)
admin.site.register(Create_Your_Own_Food)
admin.site.register(Customize)
admin.site.register(Pick)

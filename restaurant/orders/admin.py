from django.contrib import admin

from restaurant.orders.models import *

admin.site.register(Order)
admin.site.register(OrderedItem)

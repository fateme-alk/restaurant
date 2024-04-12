from rest_framework import serializers

from restaurant.orders.models import *


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ("id",)
        depth = 1

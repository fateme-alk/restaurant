from django_filters import rest_framework as filters

from restaurant.orders.models import Order


class OrderFilterSet(filters.FilterSet):
    class Meta:
        model = Order
        fields = ["discount_code", "created_at"]

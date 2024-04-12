from rest_framework import viewsets

from restaurant.orders.api.serializers import OrderSerializer
from restaurant.orders.filters import OrderFilterSet
from restaurant.orders.models import Order


class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_class = OrderFilterSet

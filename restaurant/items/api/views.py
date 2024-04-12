from rest_framework import viewsets

from restaurant.items.api.serializers import CategorySerializer, ItemSerializer
from restaurant.items.filters import ItemFilterSet
from restaurant.items.models import Category, Item


class ItemViewset(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filterset_class = ItemFilterSet


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

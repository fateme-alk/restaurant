from django_filters import rest_framework as filters

from restaurant.items.models import Item


class ItemFilterSet(filters.FilterSet):
    class Meta:
        model = Item
        fields = ["ingredients", "categories"]

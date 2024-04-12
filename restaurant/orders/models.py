from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from restaurant.items.models import Item


class Order(models.Model):
    order_num = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    items = models.ManyToManyField(Item, through="OrderedItem")  # type: ignore
    total_price = models.DecimalField(
        max_digits=10, decimal_places=0, default=0
    )
    tax = models.PositiveIntegerField(default=9)
    discount_code = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(100)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_total_price(self):
        total = sum(
            item.quantity * item.item.price
            for item in self.ordereditem_set.all()
        )
        if self.discount_code > 0:
            total = (total * (100 - self.discount_code)) / 100  # type: ignore
        # calculate tax of order's total price
        tax = (total * self.tax) / 100
        self.total_price = total + tax  # type: ignore
        self.save()

    def __str__(self):
        return str(self.order_num)


class OrderedItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.order.calculate_total_price()

    def __str__(self):
        return f"({self.item.name} x {self.quantity}) - order num:{self.order.order_num}"

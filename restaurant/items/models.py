from django.db import models


class Category(models.Model):
    STARTER = "starter"
    MAIN_DISH = "main_dish"
    DESSERT = "dessert"
    CATEGORY_CHOICES = (
        (STARTER, "starter"),
        (MAIN_DISH, "main_dish"),
        (DESSERT, "dessert"),
    )

    name = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, unique=True
    )

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=30)
    category = models.ManyToManyField(Category)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    ingredients = models.TextField()
    preparation_time = models.IntegerField()
    # image = models.ImageFiled()

    def __str__(self):
        return self.name

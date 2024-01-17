from django.db import models
from django.utils import timezone


class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    available_quantity = models.FloatField(default=0.0)
    unit = models.CharField(
        max_length=4,
        choices=[("tbsp", "Table spoon"), ("lbs", "Pounds")],
        default="lbs",
    )
    price_per_unit = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=64)

    @property
    def recipe_requirements(self):
        return self.reciperequirement_set.all()

    @property
    def price(self):
        total = 0.0
        for r in self.recipe_requirements:
            ingredient_price = r.ingredient.price_per_unit
            total += ingredient_price * r.quantity

        return total

    def __str__(self):
        return self.name


class RecipeRequirement(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Purchase of {self.menu_item.name}"

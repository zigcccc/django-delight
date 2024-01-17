from django import forms

from .models import Ingredient, MenuItem, Purchase, RecipeRequirement


class CreateIngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"


class CreateMenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"


class CreateRecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"


class CreatePurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"

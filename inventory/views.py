from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView
from django.db.models import Sum, F
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from .forms import (
    CreateIngredientForm,
    CreateMenuItemForm,
    CreateRecipeRequirementForm,
    CreatePurchaseForm,
)


def logout_request(request):
    logout(request)
    return redirect(reverse_lazy("login"))


class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "inventory/ingredients.html"


class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    success_url = "/inventory/ingredients"
    form_class = CreateIngredientForm
    template_name = "inventory/create_ingredient.html"


class PurchaseList(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purchases.html"
    ordering = ["-timestamp"]


class PurchaseCreate(LoginRequiredMixin, CreateView):
    model = Purchase
    success_url = "/inventory/purchases"
    form_class = CreatePurchaseForm
    template_name = "inventory/create_purchase.html"


class MenuItemList(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "inventory/menu.html"


class MenuItemCreate(LoginRequiredMixin, CreateView):
    model = MenuItem
    success_url = "/inventory/menu"
    form_class = CreateMenuItemForm
    template_name = "inventory/create_menu_item.html"


class RecipeRequirementCreate(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    success_url = "/inventory/menu"
    form_class = CreateRecipeRequirementForm
    template_name = "inventory/create_recipe_requirement.html"


class InsightsView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/insights.html"

    def get_revenue(self):
        revenue = Purchase.objects.aggregate(
            total=Sum(
                F("menu_item__reciperequirement__quantity")
                * F("menu_item__reciperequirement__ingredient__price_per_unit")
            )
        )
        return revenue.get("total", 0.0)

    def get_cost(self):
        revenue = self.get_revenue()

        if revenue > 0:
            revenue *= 0.8

        return round(revenue, 2)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        revenue = self.get_revenue()
        cost = self.get_cost()

        context["revenue"] = revenue
        context["cost"] = cost
        context["profit"] = round(revenue - cost, 2)
        return context

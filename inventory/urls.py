from django.urls import path, include, re_path

from . import views

urlpatterns = [
    re_path(r"^auth/", include("django.contrib.auth.urls")),
    path("logout/", views.logout_request, name="logout"),
    path("ingredients/", views.IngredientList.as_view(), name="ingredients_list"),
    path(
        "ingredients/create/",
        views.IngredientCreate.as_view(),
        name="ingredient_create",
    ),
    path("purchases/", views.PurchaseList.as_view(), name="purchase_list"),
    path("purchases/create/", views.PurchaseCreate.as_view(), name="purchase_create"),
    path("menu/", views.MenuItemList.as_view(), name="menu_item_list"),
    path("menu/create/", views.MenuItemCreate.as_view(), name="menu_item_create"),
    path(
        "recipe-requirements/create/",
        views.RecipeRequirementCreate.as_view(),
        name="recipe_requirement_create",
    ),
    path("insights/", views.InsightsView.as_view(), name="insights"),
]

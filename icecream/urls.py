from django.urls import path
from . import views


urlpatterns = [
    path("", views.icecream, name="icecream"),
    path("", views.icecream_1, name="icecream"),

    path("create", views.product_create, name="product_create"),
    path("save", views.product_save, name="product_save"),

    path("update/<ice_id>", views.product_update, name="product_update"),
    path("edit/<ice_id>", views.product_edit, name="product_edit"),
    
    
    path("<ice_id>", views.details, name="details"),
    path("remove/<ice_id>", views.remove, name="remove"),
   
]


from django.conf.urls import include, url
from django.contrib import admin

from shoppinglist import views as ShoppingListViews

urlpatterns = [
    url(r'^$', ShoppingListViews.shoppinglist, name='shoppinglist'),
]

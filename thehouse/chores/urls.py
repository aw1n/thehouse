from django.conf.urls import include, url
from django.contrib import admin

from chores import views as ChoreViews

urlpatterns = [
    url(r'^$', ChoreViews.chores, name='chores'),
]

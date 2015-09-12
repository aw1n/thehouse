from django.conf.urls import include, url
from django.contrib import admin

from roommate import views as RoommateViews

urlpatterns = [
    url(r'^$', RoommateViews.profile, name='profile'),
]

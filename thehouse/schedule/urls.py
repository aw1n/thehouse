from django.conf.urls import include, url
from django.contrib import admin

from schedule import views as ScheduleViews

urlpatterns = [
    url(r'^$', ScheduleViews.schedule, name='schedule'),
]

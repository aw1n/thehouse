from django.conf.urls import include, url
from django.contrib import admin

from ledger import views as LedgerViews

urlpatterns = [
    url(r'^$', LedgerViews.ledger, name='ledger'),
]

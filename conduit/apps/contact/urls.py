from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .views import (
    ContactView 
)

urlpatterns = [
    url(r'^contact/$', ContactView.as_view(), name='contact'),
]
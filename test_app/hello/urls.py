from django.contrib import admin
from django.urls import path
from .views import InputView

urlpatterns = [
    path(r'', InputView.as_view(), name='index'),
]
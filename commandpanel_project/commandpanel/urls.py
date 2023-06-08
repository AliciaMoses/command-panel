from django.urls import path
from . import views

urlpatterns = [
    path('', views.script_list, name='script_list'),
]

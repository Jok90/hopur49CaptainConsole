from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/history
    path('', views.index, name="index"),
]
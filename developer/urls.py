from django.urls import path
from . import views


urlpatterns = [
    #http://localhost:8000/developers
    path('', views.index, name="developer-index")
]

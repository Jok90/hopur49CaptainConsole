from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/checkout
    path('contact_info', views.contact_info, name="contact_info"),
    path('payment_info', views.payment_info, name="payment_info"),
    path('review_info', views.review_info, name="review_info"),
    path('confirmation', views.confirmation, name="confirmation"),
]


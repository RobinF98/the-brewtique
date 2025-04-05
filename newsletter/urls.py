from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsletter, name='newsletter'),
    path('newsletter_success', views.newsletter_success, name='newsletter_success'),
]

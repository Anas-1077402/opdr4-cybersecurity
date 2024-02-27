from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register, name='register'),
    path("dashboard", views.dashboard_ervaringsdeskundige, name='ervaringsdeskundige_login'),
    path('edit_profile', views.edit_profile, name="edit_profile"),
]

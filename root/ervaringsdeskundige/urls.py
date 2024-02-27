from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register, name='register'),
    path("login", views.login_ervaringsdeskundige, name='ervaringsdeskundige_login'),
    path("dashboard", views.dashboard_ervaringsdeskundige, name='ervaringsdeskundige_login'),
]
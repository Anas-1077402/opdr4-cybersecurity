from django.urls import path
from . import views

urlpatterns = [
    path("ervaringsdeskundige/register", views.register, name='register'),
]
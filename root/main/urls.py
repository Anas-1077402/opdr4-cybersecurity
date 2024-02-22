from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("API", views.API, name="api_list_test"),
    path("API/<int:pk>", views.organisatie_details, name="organisatie_details"),
    path("API/organisatie/onderzoeken", views.lijst_onderzoeken, name="lijst_onderzoeken"),
    path("beheerder/dashboard", views.dashboard, name="dashboard"),
]

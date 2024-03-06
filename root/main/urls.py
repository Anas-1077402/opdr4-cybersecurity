from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("API", views.API, name="api_list_test"),
    path("API/<int:pk>", views.organisatie_details, name="organisatie_details"),
    path("API/organisatie/onderzoeken", views.lijst_onderzoeken, name="lijst_onderzoeken"),
    path("beheerder/dashboard", views.dashboard, name="dashboard"),
    path("beheerder/dashboard/all", views.get_dashboard, name="get_dashboard"),
    path("beheerder/dashboard/research/<int:pk>", views.research_item, name="research_items"),
    path("login", views.custom_login, name="customlogin"),
]

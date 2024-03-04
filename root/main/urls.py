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
    path("beheerder/dashboard/experience_expert/<int:pk>", views.experience_expert_item, name="experience_expert_items"),
    path("beheerder/dashboard/organization/<int:pk>", views.organization_item, name="organization_items"),
    path("beheerder/dashboard/attendance_request/<int:pk>", views.attendance_request_item, name="attendance_request_items"),
    path("login", views.custom_login, name="customlogin"),
]

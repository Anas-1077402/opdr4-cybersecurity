from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("register", views.signup, name="register"),
    path('dashboard', views.dashboard_beheerder, name="dashboard"),
    path("dashboard/all", views.get_dashboard, name="get_dashboard"),
    path("dashboard/research/<int:pk>", views.research_item, name="research_items"),
    path("dashboard/research/<int:pk>/edit", views.research_item_edit, name="research_item_edit"),
    path("dashboard/research/<int:pk>/edit/save", views.research_item_edit_save, name="research_item_edit_save"),
    path("dashboard/experience_expert/<int:pk>", views.experience_expert_item, name="experience_expert_items"),
    path("dashboard/experience_expert/<int:pk>/edit", views.experience_expert_item_edit, name="experience_expert_item_edit"),
    path("dashboard/experience_expert/<int:pk>/edit/save", views.experience_expert_item_edit_save, name="experience_expert_item_edit_save"),
    path("dashboard/organization/<int:pk>", views.organization_item, name="organization_items"),
    path("dashboard/organization/<int:pk>/edit", views.organization_item_edit, name="organization_item_edit"),
    path("dashboard/organization/<int:pk>/edit/save", views.organization_item_edit_save, name="organization_item_edit_save"),
    path("dashboard/attendance_request/<int:pk>", views.attendance_request_item, name="attendance_request_items"),
    path("dashboard/attendance_request/<int:pk>/edit", views.attendance_request_item_edit, name="attendance_request_item_edit"),
    path("dashboard/attendance_request/<int:pk>/edit/save", views.attendance_request_item_edit_save, name="attendance_request_item_edit_save"),
    path('logout', views.logout_beheerder, name="logout"),
    path('change_status/<int:user_id>/<str:action>/', views.change_status, name='change_status'),
    path('edit_profile', views.edit_profile, name="edit_profile"),
    path('onderzoeken', views.onderzoeken, name="onderzoeken"),
    path('users', views.user_list, name="user_list"),
    path('update_status/<int:onderzoeks_id>/<int:nieuwe_status>/', views.update_status, name='update_status'),
    path('bewerk_onderzoek/<int:onderzoeks_id>/', views.bewerk_onderzoek, name='bewerk_onderzoek'),
    path('verwijder_onderzoek/<int:onderzoeks_id>/', views.verwijder_onderzoek, name='verwijder_onderzoek'),
]

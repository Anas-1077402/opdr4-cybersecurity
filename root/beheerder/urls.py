from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("register", views.signup, name="register"),
    path('dashboard', views.dashboard_beheerder, name="dashboard"),
    path('logout', views.logout_beheerder, name="logout"),
    path('change_status/<int:user_id>/<str:action>/', views.change_status, name='change_status'),
    path('edit_profile', views.edit_profile, name="edit_profile"),
    path('onderzoeken', views.onderzoeken, name="onderzoeken"),
    path('users', views.user_list, name="user_list"),
    path('update_status/<int:onderzoeks_id>/<int:nieuwe_status>/', views.update_status, name='update_status'),
    path('bewerk_onderzoek/<int:onderzoeks_id>/', views.bewerk_onderzoek, name='bewerk_onderzoek'),
    path('verwijder_onderzoek/<int:onderzoeks_id>/', views.verwijder_onderzoek, name='verwijder_onderzoek'),
]

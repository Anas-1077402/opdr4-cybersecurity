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
    path('update_status/<int:onderzoeks_id>/<int:nieuwe_status>/', views.update_status, name='update_status'),
]

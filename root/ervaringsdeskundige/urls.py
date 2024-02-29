from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register, name='register'),
    path("dashboard", views.dashboard_ervaringsdeskundige, name='ervaringsdeskundige_login'),
    path('edit_profile', views.edit_profile, name="edit_profile"),
    path('logout', views.logout_ervaringsdeskundige, name="logout"),
    path('onderzoeken', views.onderzoeken, name="onderzoeken"),
    path('onderzoeken', views.onderzoeken, name="onderzoeken"),
    path('registered_investigations', views.registered_investigations, name='registered_investigations'),
    path('register_investigation_succes', views.register_investigation_succes, name='register_investigation_succes'),
    path('unsubscribe_investigation', views.unsubscribe_investigation, name='unsubscribe_investigation'),
]

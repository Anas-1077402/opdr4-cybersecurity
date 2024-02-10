from django.urls import path

from . import views

urlpatterns = [
    path("register", views.signup, name="register"),
    path('login', views.login_beheerder, name="login"),
    path('dashboard', views.dashboard_beheerder, name="dashboard")
]

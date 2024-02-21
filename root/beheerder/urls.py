from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("register", views.signup, name="register"),
    path('login-beheerder', views.login_beheerder, name="login"),
    path("login-beheerder", auth_views.LoginView.as_view(template_name='authentication/login.html'), name="login"),
    path('dashboard', views.dashboard_beheerder, name="dashboard"),
    path('logout', views.logout_beheerder, name="logout"),
    path('change_status/<int:user_id>/<str:action>/', views.change_status, name='change_status'),

]


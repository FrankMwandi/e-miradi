from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # separate URL pattern for the dashboard
    path('logout/', views.user_logout, name='logout' ),
    path('', include('django.contrib.auth.urls')),  # Include Django's authentication views
]

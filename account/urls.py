from django.urls import path
from django.contrib.auth import views as auth_view
from . import views 
from .views import user_logout

urlpatterns = [
    # using custom viewpath('login/', views.user_login, name='login'),
    path('login/', auth_view.LoginView.as_view(), name='login'),
    #path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('logout/', user_logout, name='logout'),
    path('password-change/', auth_view.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_view.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('', views.dashboard, name='dashboard' ),
]

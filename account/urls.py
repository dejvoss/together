from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # to use the custom login view uncomment the following line
    # path('login/', views.user_login, name='login'),
    # own urls for the default django authentication views
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # own urls for the custom views
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('', views.dashboard, name='dashboard'),
    # to use the default django authentication views uncomment the following line
    # path('', include('django.contrib.auth.urls'))
    path('users/', views.user_list, name='user_list'),
    path('users/follow/', views.user_follow, name='user_follow'),
    path('users/<username>', views.user_detail, name='user_detail'),

    ]

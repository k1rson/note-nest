from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.AuthLoginPageView.as_view(), name='login'),
    path('registr/', views.AuthRegistrPageView.as_view(), name='registr'),
    
    path('login/auth_email/', views.AuthEmailPageView.as_view(), name='auth_email_page'),
    path('login/auth_tg/', views.AuthTelegramPageView.as_view(), name='auth_telegram_page'),

    # fetch api - endpoints
    path('login/auth_user/', views.auth_user, name='check_login'),
    path('login/auth_email/get_encrypted_email/', views.get_encrypted_email, name='get_encypted_email'),
]
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.AuthPageView.as_view(), name='auth_page'),

    # urls for fetch api
    path('check_login/<str:username>', views.check_login, name='check_login'),
    path('check_password/', views.check_password, name='check_password'),
]
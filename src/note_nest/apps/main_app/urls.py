import django.contrib
from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    
    # endpoints for fetch api
]
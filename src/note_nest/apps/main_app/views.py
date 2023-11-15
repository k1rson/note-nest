from django.shortcuts import render

from django.views import View

from django.http import JsonResponse

from apps.auth_app.services.custom_user import CustomUserService

class HomePageView(View):
    def get(self, request):
        return render(request, 'main_app/index_main.html')
    
# endpoints functions for fetch api
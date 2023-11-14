import json

from django.shortcuts import render

from django.http import JsonResponse
from django.views import View

from .services.custom_user import CustomUserService

from constants.error_codes import *
from constants.error_messages import *

class AuthPageView(View):
    def get(self, request):
        return render(request, 'auth_app/index_auth.html')
    
# fetch api views
def check_login(request, username):
    user = CustomUserService.get_object_user('username', username)

    if not user:
        return JsonResponse({'status': 'error', 
                            'error_code': ERROR_USER_NOT_FOUND_CODE,
                            'error_message': ERROR_USER_NOT_FOUND})

    return JsonResponse({'status': 'success', 
                         'id': user.pk,
                         'username': user.username,
                         'password': user.password})
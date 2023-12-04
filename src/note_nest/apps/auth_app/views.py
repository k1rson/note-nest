import json
import time

from django.shortcuts import render

from django.http import JsonResponse
from django.views import View

from .utils import get_data_from_body_request
from .services.custom_user import CustomUserService

from constants.error_codes import *
from constants.error_messages import *


class AuthLoginPageView(View):
    def get(self, request):
        return render(request, 'auth_app/login_auth.html')
    
class AuthRegistrPageView(View):
    def get(self, request):
        return render(request, 'auth_app/registr_auth.html')
    
class AuthEmailPageView(View):
    def get(self, request):
        return render(request, 'auth_app/email_auth.html')
    
class AuthTelegramPageView(View):
    def get(self, request):
        return render(request, 'auth_app/telegram_auth.html')
    
# fetch api views
def auth_user(request):
    data = get_data_from_body_request(request)
    username = data.get('username')
    password = data.get('password')
    
    user = CustomUserService.get_object_user('username', username)

    if not user:
        return JsonResponse({'status': 'error', 
                            'error_code': ERROR_USER_NOT_FOUND_CODE,
                            'error_message': ERROR_USER_NOT_FOUND})

    status_password = CustomUserService.is_correct_password(user, password)        
    if not status_password:
        return JsonResponse({'status': 'error', 
                            'error_code': ERROR_USER_INCORRECT_PASSWORD_CODE,
                            'error_message': ERROR_USER_INCORRECT_PASSWORD})
        
    is_enabled_email_auth = CustomUserService.get_email_confirmation_flag(user)
    is_enabled_telegram_auth = CustomUserService.get_telegram_confirmation_flag(user) 
    
    response_data = {
        'status': 'success',
        'is_enabled_email_auth': is_enabled_email_auth,
        'is_enabled_telegram_auth': is_enabled_telegram_auth
    }
        
    response = JsonResponse(response_data)
    response.set_cookie('username', username)

    return response

    # ВЫНЕСТИ ОТСЮДА    
    status_auth = CustomUserService.authorize_user_in_system(request, user)
    if not status_auth:
        return JsonResponse({'status': 'error', 
                            'error_code': ERROR_USER_ERROR_AUTH_CODE,
                            'error_message': ERROR_USER_ERROR_AUTH})
        
def get_encrypted_email(request): 
    data = get_data_from_body_request(request)
    username = data.get('username')
    
    user = CustomUserService.get_object_user('username', username)
    encrypted_email = CustomUserService.get_encypted_email(user)
    
    return JsonResponse({'status': 'success', 
                         'encrypted_email': encrypted_email})
    
def send_email_auth_code(request): 
    ...
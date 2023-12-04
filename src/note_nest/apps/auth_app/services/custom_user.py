from typing import Optional

from django.http import HttpRequest
from django.contrib.auth import authenticate, login

from ..models import CustomUser

class CustomUserService:
    @staticmethod
    def get_object_user(attribute: str, value: str) -> Optional[CustomUser]:
        """
        Проверяет существование пользователя по указанному атрибуту.

        :param attribute: Атрибут для поиска пользователя ('username', 'email' или 'id').
        :param value: Значение атрибута.
        :return: Объект CustomUser, если пользователь существует, иначе None.
        """
        lookup_field = {
            'id': 'id',
            'username': 'username',
            'email': 'email'
        }.get(attribute, None)

        if not lookup_field: 
            return None 
        
        try: 
            user = CustomUser.objects.get(**{lookup_field: value})
            return user
        except CustomUser.DoesNotExist:
            return None
        except CustomUser.MultipleObjectsReturned:
            return None
    
    @staticmethod
    def is_correct_password(user: CustomUser, entered_password: str) -> bool:
        """
        Проверяет, соответствует ли введенный пользователем пароль учетной записи.

        :param user: Объект пользователя
        :param entered_password: Введенный пользователем пароль для проверки.
        :return: Тип bool, характеризующее статус проверки пароля
        """
        if user.check_password(entered_password):
            return user
        else:
            return False

    @staticmethod
    def authorize_user_in_system(request: HttpRequest, user: CustomUser) -> bool: 
        """
        Авторизовывает пользователя в системе.

        :param request: Объект запроса
        :param user: Объект пользователя
        :return: Тип bool, характеризующее статус авторизации
        """
        try: 
            authenticate(request)
            login(request, user)
            
            return True
        except: 
            return False

    @staticmethod
    def get_email_confirmation_flag(user: CustomUser) -> bool:
        """
        Возвращает флаг, указывающий, подключенна ли доп. аутентификация через email

        :param user: Объект пользователя
        :return: Тип bool, указывающий, подключена ли доп. аутентификация через email
        """
        return user.is_enabled_email_auth

    @staticmethod
    def get_telegram_confirmation_flag(user: CustomUser) -> bool:
        """
        Возвращает флаг, указывающий, подключенна ли доп. аутентификация через telegram бота

        :param user: Объект пользователя
        :return: Тип bool, указывающий, подключена ли доп. аутентификация через telegram бота
        """
        return user.is_enabled_telegram_auth

    @staticmethod
    def get_encypted_email(user: CustomUser) -> str: 
        """
        Возвращает строку с зашифрованной почтой в виде (a***n@bk.ru)

        :param user: Объект пользователя
        :return: Строка, содержащая зашифрованную почту
        """
        email = user.email
        
        username, domain = email.split('@')
        encrypted_username = username[0] + '*' * (len(username) - 2) + username[-1]
        
        return f"{encrypted_username}@{domain}"
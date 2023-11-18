import json

from typing import Optional


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
    
    def check_correct_password(username: str, entered_password: str) -> bool:
        """
        Проверяет, соответствует ли введенный пользователем пароль учетной записи.

        :param user: Введенный пользователем username
        :param entered_password: Введенный пользователем пароль для проверки.
        :return: Объект CustomUser, если пароль корректен, в противном случае None.
        """
        user = CustomUser.objects.get(username=username)
        
        if user.check_password(entered_password):
            return user
        else:
            return None
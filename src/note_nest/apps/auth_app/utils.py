from django.http import HttpRequest

import json

def get_data_from_body_request(request: HttpRequest) -> dict:
    """
        Извлекает данные из тела запроса FetchAPI
        
        :param request: Объект запроса -> request
        :return: Тип dict, словарь с извлеченными данными
    """
    try: 
        data = json.loads(request.body)
        return data
    except json.JSONDecodeError:
        return None
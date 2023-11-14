function check_response(response) {
    if(response.ok){
        return response.json()
            .then(function(parsed_response){
                return (parsed_response.status === 'success') ? Promise.resolve(parsed_response) : Promise.reject(parsed_response);
            });
    } else {
        return Promise.reject(response);
    }
}

/**
 * Определяет тип ошибки (HTTP Error or Custom Error)
 * 
 * HTTP Error - стандартные ошибки протокола HTTP: 404, 403, 500 и т.д.
 * Custom Error - кастомные ошибки, отправленные посредством JsonResponse (ERROR_USER_NOT_FOUND и т.д.)
 * 
 * @param {Response} response - Объект ответа от сервера
 */
function detect_error(response) {
    if(response.status !== 'error' && response.status !== 'success') {
        call_toast('Ошибка', 3, `Ошибка! Код ошибки: ${response.status}`);
    } else{
        call_toast('Ошибка', 3, response.error_message);
    }
}

/**
 * Отображает всплывающее уведомление (toast).
 *
 * @param {string} type_toast_text - Текст, описывающий тип уведомления.
 * @param {number} type_icon_number - Номер типа иконки (1 - успех, 2 - предупреждение, 3 - ошибка).
 * @param {string} message - Сообщение, которое будет отображаться в уведомлении.
 */
function call_toast(type_toast_text, type_icon_number, message){
    let toast_live_object = document.getElementById('live-toast')

    let toast_type = document.getElementById('toast-type')
    let toast_content = document.getElementById('toast-content')
    let toast_icon = document.getElementById('toast-icon')

    let icon_path;
    switch (type_icon_number) {
        case 1:
            icon_path = success_icon
            break;
        case 2:
            icon_path = warning_icon
            break;
        case 3:
            icon_path = error_icon
            break;
    }

    toast_type.innerText = type_toast_text
    toast_content.innerText = message
    toast_icon.src = icon_path

    let toast = new bootstrap.Toast(toast_live_object)
    toast.show()
}

/**
 * Извлекает необходимый параметр из cookie Django
 *
 * @param {string} name - Название извлекаемого параметра.
 */
function get_cookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
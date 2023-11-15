function check_login_fetch(username){
    const url = `check_login/${encodeURIComponent(username)}`;

    fetch(url)
        .then(check_response)
        .then(function(parsedResponse){
        })
        .catch(detect_error)
}
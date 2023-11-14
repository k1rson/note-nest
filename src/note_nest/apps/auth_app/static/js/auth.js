// delimiters: ['[[', ']]'] - for django

function check_login(username){
    const url = `check_login/${encodeURIComponent(username)}`;

    fetch(url)
        .then(check_response)
        .then(function(parsedResponse){
            console.log(parsedResponse);
        })
        .catch(detect_error)
}
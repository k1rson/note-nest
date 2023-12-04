// vue components 

// vue apps
const auth_email_app = {
    data() {
        return {
            username: '', 
            encrypted_email: ''
        }
    }, 
    components: {

    }, 
    beforeMount() {
        this.username = get_cookie('username');
        this.get_encypted_email();
      },
    methods: {
        get_encypted_email(){ 
            const url = `get_encrypted_email/`

            let post_data = {
                username: this.username
            }

            const csrf_token = get_cookie('csrftoken');
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrf_token,
                },
                body: JSON.stringify(post_data),
            })
            .then(check_response)
            .then((response) => {
                this.encrypted_email = response.encrypted_email
            })
            .catch(detect_error); 
        }
        
    }
}

// initalization vue apps
Vue.createApp(auth_email_app).mount('#auth_email_app')
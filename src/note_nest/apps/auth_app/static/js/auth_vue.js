// vue components 

// vue app 
const auth_app = {
    data () {
        return {
            login: '', 
            password: '', 
            is_disabled_button: true, 
        }
    },
    methods: {
        check_login() {
            const url = `check_login/${encodeURIComponent(this.login)}`;
        
            fetch(url)
                .then(check_response)
                .then(() => {
                    this.toggle_button_state();
                })
                .catch(detect_error)
        },
        check_password() {
            const url = `check_password/`;
            
            let post_data = {
                username: this.login, 
                password: this.password
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
              .then(() => {
                console.log('ok')
              })
              .catch(detect_error)

        }, 
        toggle_button_state() {
            this.is_disabled_button = !this.is_disabled_button
        }
    }
}

const switch_logo_app = {
    data () {
        return {

        }
    }
}

// vue initializer 
Vue.createApp(auth_app).mount('#auth_app')
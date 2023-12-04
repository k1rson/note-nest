// vue apps
const auth_app = {
    data() {
      return {
        login: '',
        password: '',
        loading: false
      };
    },
    methods: {
      auth_user() {
        this.loading = true; 
  
        const url = `auth_user/`;
  
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
          .then((response) => {
            let redirect_url = '';
  
            if (response.is_enabled_email_auth) {
              redirect_url = `auth_email/`;
            } else if (response.is_enabled_telegram_auth) {
              redirect_url = `auth_tg/`;
            } else {
              redirect_url = '';
            }
  
            window.location.href = redirect_url;
          })
          .catch(detect_error)
          .finally(() => {
            this.loading = false; 
          });
      }
    }
}

// initializer vue apps
Vue.createApp(auth_app).mount('#auth_app')
  
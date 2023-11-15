// vue components

// apps
const app_likes_dislikes = {
    data() {
        return { 
            user_list: [], // Используйте массив для хранения пользователей
        };
    },
    created() {
    }
}

// initialize apps
Vue.createApp(app_likes_dislikes).mount('#app_likes_dislikes')
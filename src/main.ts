import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// Main style
require('@/assets/styles/main.scss');
// require('bootstrap/dist/js/bootstrap.bundle.min.js');

createApp(App)
    .use(store)
    .use(router)
    .mount('#app')

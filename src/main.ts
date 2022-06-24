import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { APIService } from './common/api.service'

import { createPinia } from 'pinia'

// Main style
require('@/assets/styles/main.scss');
// require('bootstrap/dist/js/bootstrap.bundle.min.js');

// Initialize service
APIService.init()

createApp(App)
    .use(router)
    .use(createPinia())
    .mount('#app')

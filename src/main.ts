import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'


// Main style
import './assets/styles/main.scss'

import { APIService } from '@/common/api.service'

// Initialize service
APIService.init()

const app = createApp(App)

app.use(createPinia())
app.use(router)


app.mount('#app')
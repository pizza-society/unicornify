import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    components: {
      default: () =>  import('@/views/HomeView.vue'),
      Navbar: () => import('@/components/navbars/NavbarMain.vue')
    }
  },
  {
    path: '/about',
    name: 'about',
    components: {
      default:() => import('@/views/AboutView.vue'),
      Navbar: () => import('@/components/navbars/NavbarMain.vue')
    }
  },
  {
    path: '/email-validator',
    name: 'EmailValidator',
    components: {
      default:() => import('@/views/24hTo12hConverter.vue'),
      Navbar: () => import('@/components/navbars/NavbarMain.vue')
    }
  },
  {
    path: '/testing',
    name: 'testing',
    components: {
      default:() => import('@/views/TestingView.vue'),
      Navbar: () => import('@/components/navbars/NavbarMain.vue')
    }
  },
  {
    path: '/qr-code-generator',
    name: 'qr-code-generator',
    components: {
      default:() => import('@/views/QRGeneratorView.vue'),
      Navbar: () => import('@/components/navbars/NavbarMain.vue')
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

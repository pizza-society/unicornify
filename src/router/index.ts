import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    components: {
      default: () => HomeView,
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
    path: '/24h-to-12h',
    name: '24hTo12hConverter',
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
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

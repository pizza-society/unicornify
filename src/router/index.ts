import { createRouter, createWebHistory } from 'vue-router'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
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
      path: '/24h-to-12h',
      name: '24hTo12hConverter',
      components: {
        default:() => import('@/views/24hTo12hConverter.vue'),
        Navbar: () => import('@/components/navbars/NavbarMain.vue')
      }
    },
    {
      path: '/email-validator',
      name: 'EmailValidator',
      components: {
        default:() => import('@/views/EmailValidatorView.vue'),
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
    },
    {
      path: '/twitter-downloader',
      name: 'twitter-downloader',
      components: {
        default:() => import('@/views/TwitterDownloaderView.vue'),
        Navbar: () => import('@/components/navbars/NavbarMain.vue')
      }
    },
    {
      path: '/calendar-link-generator',
      name: 'calendar-link-generator',
      components: {
        default:() => import('@/views/CalendarLinkGeneratorView.vue'),
        Navbar: () => import('@/components/navbars/NavbarMain.vue')
      }
    }
  ]
})


export default router

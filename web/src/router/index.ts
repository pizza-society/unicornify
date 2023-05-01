import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
const ROOT_ROUTE = '/home'

const routes: Array<RouteRecordRaw> = [
	{
		path: '/',
		name: 'home',
		meta: { title: 'Home' },
		components: {
			default: () => import('@/views/HomeView.vue'),
			Navbar: () => import('@/components/navbars/NavbarMain.vue')
		}
	},
	{
		path: '/about',
		name: 'about',
		meta: { title: 'About' },
		components: {
			default: () => import('@/views/AboutView.vue'),
			Navbar: () => import('@/components/navbars/NavbarMain.vue')
		}
	},
	{
		path: '/clock-converter',
		name: 'clock-converter',
		meta: { title: 'Clock Converter' },
		components: {
			default: () => import('@/views/ClockConverterView.vue'),
			Navbar: () => import('@/components/navbars/NavbarMain.vue')
		}
	},
	{
		path: '/email-validator',
		name: 'email-validator',
		meta: { title: 'Email Validator' },
		components: {
			default: () => import('@/views/EmailValidatorView.vue'),
			Navbar: () => import('@/components/navbars/NavbarMain.vue')
		}
	},
	{
		path: '/testing',
		name: 'testing',
		meta: { title: 'Testing' },
		components: {
			default: () => import('@/views/TestingView.vue'),
			Navbar: () => import('@/components/navbars/NavbarMain.vue')
		}
	},
	{
		path: '/qr-code-generator',
		name: 'qr-code-generator',
		meta: { title: 'QR Code Generator' },
		components: {
			default: () => import('@/views/QRGeneratorView.vue'),
			Navbar: () => import('@/components/navbars/NavbarMain.vue')
		}
	},
	{
		path: '/twitter-downloader',
		name: 'twitter-downloader',
		meta: { title: 'Twitter Downloader' },
		components: {
			default: () => import('@/views/TwitterDownloaderView.vue'),
			Navbar: () => import('@/components/navbars/NavbarMain.vue')
		}
	},
	{
		path: '/calendar-link-generator',
		name: 'calendar-link-generator',
		meta: { title: 'Calendar Link Generator' },
		components: {
			default: () => import('@/views/CalendarLinkGeneratorView.vue'),
			Navbar: () => import('@/components/navbars/NavbarMain.vue')
		}
	}
]

const router = createRouter({
	history: createWebHistory(),
	routes
})


/**
 * RouterGuard
 */

router.afterEach((to, from, failure) => {
	if (to.meta.title && failure?.from.path !== ROOT_ROUTE) {
	// Only update page title if no failure
		document.title = `Unicornify - ${ to.meta.title }`
	}
})

export default router

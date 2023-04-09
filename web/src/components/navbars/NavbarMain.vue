<template>
	<nav class="navbar navbar-dark navbar-expand-lg bg-dark shadow">
		<div class="container-fluid">
			<a
				class="navbar-brand"
				href="#">
				<img
					alt="site_logo"
					src="@/assets/images/pizza-slice.png"
					class="d-inline-block align-text-top navbar-brand-logo" />
			</a>

			<button
				id="menu-icon"
				class="navbar-toggler border-0 shadow-none"
				type="button"
				aria-label="Toggle navigation"
				:class="{
					'open': isMobMenuOpen
				}"
				@click="toggleMobMenu()">
				<span></span>
				<span></span>
				<span></span>
				<span></span>
			</button>

			<div
				class="collapse navbar-collapse"
				:class="{ 'show': isMobMenuOpen }">
				<NavbarNav
					:items="menuItem"
					@on-mobile-click="toggleMobMenu()" />
				<div class="navbar-nav ms-auto mt-3 mt-sm-0">
					<a
						class="btn btn-outline-primary github-desktop"
						href="https://github.com/pizza-society/unicornify"
						target="_blank">
						<i class="fa-brands fa-github-alt"></i>
						Github
					</a>

					<p class="github-mobile text-center">
						<a
							class="text-secondary"
							href="https://github.com/pizza-society/unicornify"
							target="_blank">
							<i class="fa-brands fa-github-alt fa-xl"></i>
						</a>
					</p>
				</div>
			</div>
		</div>
	</nav>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

import { NavbarItem } from '@/common/navbar'
import NavbarNav from '@/components/navbars/NavbarNav.vue'

export default defineComponent({
	name: 'NavbarMain',
	components: {
		NavbarNav
	},
	setup() {
		// Data
		const isMobMenuOpen = ref<boolean>(false)
		const menuItem = ref<NavbarItem[]>([
			{
				title: 'Home',
				name: 'home',
				path: '/'
			}, 
			{
				title: 'About',
				name: 'about',
				path: '/about'
			}, 
			{
				title: 'Downloaders',
				name: 'downloaders',
				dropdown: [
					{
						title: 'Twitter Video',
						path: '/twitter-downloader'
					}
				]
			}, 
			{
				title: 'Generators',
				name: 'generators',
				dropdown: [
					{
						title: 'Calendar Link',
						path: '/calendar-link-generator'
					},
					{
						title: 'QR Code',
						path: '/qr-code-generator'
					}
				]
			}, 
			{
				title: 'Validators',
				name: 'validators',
				dropdown: [
					{
						title: 'Email',
						path: '/email-validator'
					}
				]
			}, 
			{
				title: 'Others',
				name: 'others',
				dropdown: [
					{
						title: 'Clock Converter',
						path: '/clock-converter'
					}
				]
			}
		])

		const toggleMobMenu = () => {
			isMobMenuOpen.value = !isMobMenuOpen.value
		}

		return {
			isMobMenuOpen,
			menuItem,
			toggleMobMenu
		}
	}
})
</script>

<style lang="scss" scoped>
	@media (max-width: 576px) {
		.collapse.navbar-collapse {
			background-color: #212529;
			height: 100vh;
			width: calc(100% - 1.5rem);
			padding-right: 2.5rem;
			padding-left: 2.5rem;
			padding-top: 0;
			position: fixed;
			top: 6rem;
			z-index: 1050;

			:deep(.navbar-nav .nav-link){
				border-bottom: 1px solid #343a40;
			}
		}

		.github-mobile {
			display: block;
		}

		.github-desktop {
			display: none;
		}

		#menu-icon {
			width: 15px;
			height: 15px;
			position: relative;
			margin-top: auto;
			margin-bottom: auto;
			margin-left: auto;
			margin-right: 0;
			-webkit-transform: rotate(0deg);
			-moz-transform: rotate(0deg);
			-o-transform: rotate(0deg);
			transform: rotate(0deg);
			-webkit-transition: .5s ease-in-out;
			-moz-transition: .5s ease-in-out;
			-o-transition: .5s ease-in-out;
			transition: .5s ease-in-out;
		}

		#menu-icon span {
			display: block;
			position: absolute;
			height: 0.2rem;
			width: 100%;
			background: #ffffff80;
			border-radius: 0.2rem;
			opacity: 1;
			left: 0;
			-webkit-transform: rotate(0deg);
			-moz-transform: rotate(0deg);
			-o-transform: rotate(0deg);
			transform: rotate(0deg);
			-webkit-transition: .25s ease-in-out;
			-moz-transition: .25s ease-in-out;
			-o-transition: .25s ease-in-out;
			transition: .25s ease-in-out;
		}

		#menu-icon span:nth-child(1) {
			top: 0px;
		}

		#menu-icon span:nth-child(2),#menu-icon span:nth-child(3) {
			top: 0.4rem;
		}

		#menu-icon span:nth-child(4) {
			top: 0.8rem;
		}

		#menu-icon.open span:nth-child(1) {
			top: 0.4rem;
			width: 0%;
			left: 50%;
		}

		#menu-icon.open span:nth-child(2) {
			-webkit-transform: rotate(45deg);
			-moz-transform: rotate(45deg);
			-o-transform: rotate(45deg);
			transform: rotate(45deg);
		}

		#menu-icon.open span:nth-child(3) {
			-webkit-transform: rotate(-45deg);
			-moz-transform: rotate(-45deg);
			-o-transform: rotate(-45deg);
			transform: rotate(-45deg);
		}

		#menu-icon.open span:nth-child(4) {
			top: 0.4rem;
			width: 0%;
			left: 50%;
		}
	}

	@media (min-width: 576px) {
		.github-mobile {
			display: none;
		}

		.github-desktop {
			display: block;
		}
	}
</style>
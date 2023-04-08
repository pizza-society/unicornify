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
				class="navbar-toggler"
				type="button"
				data-bs-toggle="collapse"
				data-bs-target="#navbarMenu"
				aria-controls="navbarMenu"
				aria-expanded="false"
				aria-label="Toggle navigation">
				<span class="navbar-toggler-icon"></span>
			</button>

			<div
				id="navbarMenu"
				class="collapse navbar-collapse">
				<NavbarNav :items="menuItem" />
				<div class="navbar-nav ms-auto">
					<a
						class="btn btn-outline-primary"
						href="https://github.com/pizza-society/unicornify"
						target="_blank">
						<i class="fa-brands fa-github-alt"></i>
						Github
					</a>
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

		return {
			menuItem
		}
	}
})
</script>

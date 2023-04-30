<template>
	<router-view name="Navbar" />
	<div class="bg-dark">
		<router-view class="container-fluid vh-min text-white" />
		<TheToast />
	</div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import TheToast from './components/overlays/TheToast.vue'

const lottieWebPlayerScript = document.createElement('script')
const lottiePlayerUrl = 'https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js'

onMounted(() => {
	lottieWebPlayerScript.setAttribute('src', lottiePlayerUrl)  // Add Lottie web player script to main app
	document.head.appendChild(lottieWebPlayerScript)
})
</script>

<style lang="scss">
.vh-min {
  min-height: calc(100vh - 3.9rem) !important;
}
</style>

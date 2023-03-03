<template>
  <router-view name="Navbar" class="is-family-monospace" />
  <div class="bg-dark is-family-monospace">
    <router-view class="container-fluid vh-min text-white"/>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'

let lottieWebPlayerScript = document.createElement('script')

onMounted(() => {
  lottieWebPlayerScript.setAttribute('src', 'https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js')  // Add Lottie web player script to main app
  document.head.appendChild(lottieWebPlayerScript)
})
</script>


<style lang="scss">
.vh-min {
  min-height: calc(100vh - 3.9rem) !important;
}

</style>

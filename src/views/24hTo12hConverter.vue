<template>
  <div class="container">
    <div class="d-flex flex-column vh-min justify-content-center align-items-center">
        <img src="@/assets/images/outer-space.svg"
          style="height: 30rem; width:auto">
        <p>
          Phew phew Simple 24 H to 12 H converter
        </p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: '24h-to-12h-converter',
  setup() {
    return {}
  }
});
</script>

<style lang="scss" scoped>
</style>

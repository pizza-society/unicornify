<template>
  <MainNavbar></MainNavbar>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import MainNavbar from '@/components/navbars/MainNavbar.vue';

export default defineComponent({
  name: 'HomeView',
  components: {
    MainNavbar
  },
});
</script>

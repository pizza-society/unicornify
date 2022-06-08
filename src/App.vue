<template>
  <router-view name="Navbar" class="is-family-monospace" />
  <div class="bg-dark is-family-monospace">
    <router-view class="container-fluid vh-min text-white"/>
  </div>
</template>

<style lang="scss">
.vh-min {
  min-height: calc(100vh - 3.9rem) !important;
}

</style>

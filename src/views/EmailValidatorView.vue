<template>
  <div class="container">
    <div class="d-flex flex-column justify-content-center align-items-center">
        <!-- <img src="@/assets/images/outer-space.svg"
          style="height: 30rem; width:auto"> -->
        <h1>
          <b>Email Address Validator</b>
        </h1>
        <span >
          <lottie-player src="https://assets3.lottiefiles.com/packages/lf20_ebqz3ltq.json"  background="transparent"  speed="1"   style="width: 300px; height: 300px;"  loop  autoplay></lottie-player>
        </span>
        <p>
          Email Validator is A Simple Little Tool for Validating and Detecting Real/Disposable and Temporary Email Addresses.
        </p>
        <b>Add an email address below to verify its validity in real - time basis.</b>
    </div>
    <div class="container-sm">
      <div>
        <div class="input-group  mt-4">
          <input type="text" class="form-control" placeholder="Email address" aria-label="Email address" aria-describedby="button-addon1">
          <button class="btn btn-outline-primary" type="button" id="button-addon1">Verify</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  name: "add-tutorial",
  data() {
    return {
    };
  },
  methods: {
  },
});
</script>
<style lang="scss">
.container-sm {
  max-width: 25rem;
}

.container {
  max-width: 50rem;
  padding-top: 5rem;
}

</style>
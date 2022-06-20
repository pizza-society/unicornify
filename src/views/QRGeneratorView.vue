<template>
    <div class="container">
        <div class="d-flex flex-row vh-min justify-content-center align-items-center row">
            <div class="col-sm-12 col-md-4 text-center">
                <div class="mb-3">
                    <label class="form-label">Enter URL</label>
                    <input class="form-control"
                        placeholder="Enter link to open when scanned"
                        :disabled="isLoading" />
                </div>
                <button class="btn btn-primary"
                    v-on:click="generateQR()">
                    <span v-if="!isLoading">
                        Generate
                    </span>
                    <span v-else>
                        <i class="fa-solid fa-spinner fa-spin"></i>
                    </span>
                </button>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

export default defineComponent({
    name: 'QRGeneratorView',
    setup() {
        const isLoading = ref<boolean>(false)

        const generateQR = () => {
            isLoading.value = true

            setTimeout( () => {
                isLoading.value = false
            }, 5000)
        }

        return {
            isLoading,
            generateQR
        }
    },
})
</script>
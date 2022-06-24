<template>
    <div class="container">
        <div class="d-flex flex-row vh-min justify-content-center align-items-center row">
            <div class="col-sm-12 col-md-4 text-center">
               <div class="mb-3">
                    <div class="mb-3">
                        <label class="form-label">Enter URL</label>
                        <input class="form-control"
                            placeholder="Enter link to open when scanned"
                            v-model="urlForm.link"
                            :disabled="isLoading" />
                    </div>
                    <button class="btn btn-primary"
                        v-on:click="generateQR()"
                        :disabled="isLoading ||
                            urlForm.link === null ||
                            urlForm.link === ''">
                        <span v-if="!isLoading">
                            Generate
                        </span>
                        <span v-else>
                            <i class="fa-solid fa-spinner fa-spin"></i>
                        </span>
                    </button>
               </div>

                <img v-if="generatedResult" 
                    :src="`data:image/jpg;base64,${generatedResult}`" />
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useServiceStore } from '@/store';

export default defineComponent({
    name: 'QRGeneratorView',
    setup() {
        const isLoading = ref<boolean>(false)
        const generatedResult = ref<string | null | unknown>(null)
        const serviceSvc = useServiceStore()
        const urlForm = ref({
            link: null
        })

        const generateQR = () => {
            isLoading.value = true

            return serviceSvc.generateQR(
                urlForm.value
            ).then(data => {
                generatedResult.value = data
                isLoading.value = false
            }).catch(() => {
                isLoading.value = false
            })
        }

        const isValidHttpUrl = () => {
            let url

            try {
                url = new URL(String(urlForm.value.link))
            } catch (_) {
                return false
            }

            return url.protocol === 'http:' || url.protocol === 'https:'
        }

        return {
            isLoading,
            generateQR,
            urlForm,
            generatedResult,
            isValidHttpUrl
        }
    },
})
</script>
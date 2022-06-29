<template>
    <div class="container">
        <div class="d-flex flex-row vh-min justify-content-center align-items-center row">
            <div class="col-sm-12 col-md-4 text-center">
               <div class="mb-3">
                    <form class="needs-validation mb-3">
                        <label class="form-label">Enter URL</label>
                        <input class="form-control"
                            placeholder="Enter link to open when scanned"
                            v-model="urlForm.link"
                            :disabled="isLoading"
                            @blur="v$.link.$touch"
                            :class="{
                                'is-invalid': v$.link.$error && v$.link.$dirty,
                                'is-valid': !v$.link.$error && v$.link.$dirty
                            }" />
                            <div class="invalid-feedback" 
                                v-for="error of v$.link.$errors"
                                :key="error.$uid">
                                {{ error.$message }}
                            </div>
                    </form>

                    <div class="d-grid gap-2 d-flex justify-content-center">
                        <button class="btn btn-primary"
                            v-on:click="generateQR()"
                            :disabled="isLoading || v$.$invalid">
                            <span v-if="!isLoading">
                                Generate
                            </span>
                            <span v-else>
                                <i class="fa-solid fa-spinner fa-spin"></i>
                            </span>
                        </button>

                        <button class="btn btn-primary"
                            v-on:click="reset()"
                            :disabled="generatedResult === null"
                            v-if="generatedResult !== null">
                            <span>
                                Reset
                            </span>
                        </button>
                    </div>

                    
               </div>

                <img v-if="generatedResult" 
                    :src="`data:image/jpg;base64,${generatedResult}`"
                    class="rounded" />
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useServiceStore } from '@/store';

import useVuelidate from '@vuelidate/core'
import { helpers, required, url } from '@vuelidate/validators'

export default defineComponent({
    name: 'QRGeneratorView',
    setup() {

        // Data
        const generatedResult = ref<string | null | unknown>(null)

        // Service
        const serviceSvc = useServiceStore()

        // Form
        const urlForm = ref({
            link: null
        })
        const validation = {
            link: { 
                required: helpers.withMessage(
                    'Need to have a value',
                    required
                ),
                url: helpers.withMessage(
                    'Need to have a valid url',
                    url
                )}
        }
        const v$ = useVuelidate(validation, urlForm)

        // Checker
        const isLoading = ref<boolean>(false)

        // Generate QR
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

        // Reset service
        const reset = () => {
            v$.value.$reset()
            urlForm.value.link = null
            generatedResult.value = null
        }

        return {
            generatedResult,
            urlForm,
            v$,
            isLoading,
            generateQR,
            reset
        }
    },
})
</script>
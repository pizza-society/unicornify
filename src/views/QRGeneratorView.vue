<template>
    <div class="container">
        <div class="d-flex flex-row vh-min justify-content-center align-items-center row">
            <div class="col-sm-12 col-md-4 text-center">
                <div class="mb-3">
                    <form class="needs-validation">
                        <div class="mb-3">
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
                        </div>
                    </form>

                    <button class="btn btn-primary text-center mb-3"
                        v-on:click="generateQR()"
                        :disabled="isLoading || v$.$invalid">
                        <span v-if="!isLoading">
                            Generate
                        </span>
                        <span v-else>
                            <i class="fa-solid fa-spinner fa-spin"></i>
                        </span>
                    </button>

                    <div class="d-grid gap-2 d-flex justify-content-center">
                        <button class="btn btn-outline-primary"
                            v-on:click="toggleModal()"
                            :disabled="isLoading">
                            Design
                        </button>

                        <button class="btn btn-outline-primary"
                            v-on:click="reset()"
                            :disabled="generatedResult === null"
                            v-if="generatedResult !== null">
                            <span>
                                Reset
                            </span>
                        </button>
                    </div>
                </div>
            </div>

            <Transition>
                <div class="col-sm-12 col-md-3 text-center"
                    v-if="generatedResult" >
                    <div class="card bg-transparent">
                        <div class="card-body shadow">
                            <img v-if="generatedResult" 
                                :src="`data:image/png;base64,${generatedResult}`"
                                class="rounded w-100 mb-3" />
                            <div class="d-grid gap-2 d-flex justify-content-center">
                                <button class="btn btn-outline-primary"
                                    v-on:click="download()">
                                    <i class="fa-solid fa-download"></i>
                                    Download {{ urlForm.imageType.toUpperCase() }}
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </Transition>
        </div>

        <ModalComponent ref="modalComponent">
            <template #header>
                <span>
                    Customize design
                </span>
            </template>

            <template #content>
                <form class="needs-validation">
                    <div>
                        <label class="form-label">Image type</label>
                        <select class="form-select" v-model="urlForm.imageType">
                            <option :value="ImageChoices.JPEG">
                                JPEG
                            </option>
                            <option :value="ImageChoices.PNG">
                                PNG
                            </option>
                        </select>
                    </div>

                    <hr class="my-3" />

                    <div class="row">
                        <div class="col-6">
                            <label class="form-label">Front color</label>
                            <input type="color"
                                class="form-control form-control-color"
                                v-model="urlForm.frontColor" />
                        </div>

                        <div class="col-6">
                            <label class="form-label">Back color</label>
                            <input type="color"
                                class="form-control form-control-color"
                                v-model="urlForm.backColor" />
                        </div>
                    </div>
                </form>
            </template>

            <template #footer>
                <button type="button"
                    class="btn btn-outline-primary"
                    v-on:click="toggleModal()">
                    Close
                </button>
                <button type="button"
                    class="btn btn-primary"
                    v-on:click="toggleModal()">
                    Save changes
                </button>
            </template>
        </ModalComponent>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useServiceStore } from '@/store';

import { ImageChoices } from '@/helpers/qr_generator.enum';
import ModalComponent from '@/components/ModalComponent.vue';

import useVuelidate from '@vuelidate/core';
import { helpers, required, url } from '@vuelidate/validators';

export default defineComponent({
    name: 'QRGeneratorView',
    setup() {

        // Data
        const generatedResult = ref<string | null | unknown>(null)

        // Services
        const serviceSvc = useServiceStore()

        // Forms
        const urlForm = ref({
            link: null,
            imageType: ImageChoices.JPEG,
            frontColor: '#000000',
            backColor: '#ffffff'
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

        // Checkers
        const isLoading = ref<boolean>(false)

        // Components
        const modalComponent = ref<InstanceType<typeof ModalComponent>>()

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

        // Download output
        const download = () => {
            const filetype_ = urlForm.value.imageType
            const source = `data:image/${filetype_};base64,${generatedResult.value}`
            const fileName = `qrcode_`
            const downloadLink = document.createElement('a')
            downloadLink.href = source
            downloadLink.download = `${fileName}.${filetype_}`
            downloadLink.click()
        }

        const toggleModal = () => {
            modalComponent.value?.toggleModal()
        }

        return {
            generatedResult,
            urlForm,
            v$,
            isLoading,
            modalComponent,
            generateQR,
            reset,
            download,
            toggleModal,
            ImageChoices
        }
    },
    components: {
        ModalComponent
    },
})
</script>

<style lang="scss" scoped>
.v-enter-active,
.v-leave-active {
  transition: all .2s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}

.v-enter-from {
    transform: translateX(10px);
    opacity: 0;
}
.v-leave-to {
    transform: translateX(10px);
    opacity: 0;
}
</style>
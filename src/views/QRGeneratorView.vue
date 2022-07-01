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
                                v-model="qrForm.url"
                                :disabled="isLoading"
                                @blur="v$.url.$touch"
                                :class="{
                                    'is-invalid': v$.url.$error && v$.url.$dirty,
                                    'is-valid': !v$.url.$error && v$.url.$dirty
                                }" />
                            <div class="invalid-feedback" 
                                v-for="error of v$.url.$errors"
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
                                    Download
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
                        <select class="form-select" v-model="qrForm.imageType">
                            <option :value="ImageChoices.JPEG">
                                JPEG
                            </option>
                            <option :value="ImageChoices.PNG">
                                PNG
                            </option>
                        </select>
                    </div>

                    <hr class="my-3" />

                    <label class="form-label">Style</label>
                    <div class="row">
                        <div class="col-sm-6 col-md-4">
                            <img src="@/assets/images/qr/qr-example-1-square.png"
                                role="button"
                                class="rounded w-100 drawer-img"
                                title="Square"
                                :class="{
                                    'selected': qrForm.drawer === DrawerChoices.SQUAREM
                                }"
                                v-on:click="onSelectDrawer(DrawerChoices.SQUAREM)" />
                        </div>

                        <div class="col-sm-6 col-md-4">
                            <img src="@/assets/images/qr/qr-example-2-gapped.png"
                                role="button"
                                class="rounded w-100 drawer-img"
                                title="Gapped square"
                                :class="{
                                    'selected': qrForm.drawer === DrawerChoices.GAPPEDM
                                }"
                                v-on:click="onSelectDrawer(DrawerChoices.GAPPEDM)" />
                        </div>

                        <div class="col-sm-6 col-md-4">
                            <img src="@/assets/images/qr/qr-example-3-circle.png"
                                role="button"
                                class="rounded w-100 drawer-img"
                                title="Circle"
                                :class="{
                                    'selected': qrForm.drawer === DrawerChoices.CIRCLEM
                                }"
                                v-on:click="onSelectDrawer(DrawerChoices.CIRCLEM)" />
                        </div>

                        <div class="col-sm-6 col-md-4">
                            <img src="@/assets/images/qr/qr-example-4-rounded.png"
                                role="button"
                                class="rounded w-100 drawer-img"
                                title="Rounded"
                                :class="{
                                    'selected': qrForm.drawer === DrawerChoices.ROUNDEDM
                                }"
                                v-on:click="onSelectDrawer(DrawerChoices.ROUNDEDM)" />
                        </div>

                        <div class="col-sm-6 col-md-4">
                            <img src="@/assets/images/qr/qr-example-5-vertical.png"
                                role="button"
                                class="rounded w-100 drawer-img"
                                title="Vertical"
                                :class="{
                                    'selected': qrForm.drawer === DrawerChoices.VERTICALM
                                }"
                                v-on:click="onSelectDrawer(DrawerChoices.VERTICALM)" />
                        </div>

                        <div class="col-sm-6 col-md-4">
                            <img src="@/assets/images/qr/qr-example-6-horizontal.png"
                                role="button"
                                class="rounded w-100 drawer-img"
                                title="Horizontal"
                                :class="{
                                    'selected': qrForm.drawer === DrawerChoices.HORIZONTALM
                                }"
                                v-on:click="onSelectDrawer(DrawerChoices.HORIZONTALM)" />
                        </div>
                    </div>

                    <hr class="my-3" />

                    <div class="row">
                        <div class="col-6">
                            <label class="form-label">Front color</label>
                            <input type="color"
                                class="form-control form-control-color p-0"
                                v-model="qrForm.frontColor" />
                        </div>

                        <div class="col-6">
                            <label class="form-label">Back color</label>
                            <input type="color"
                                class="form-control form-control-color p-0"
                                v-model="qrForm.backColor" />
                        </div>
                    </div>
                </form>
            </template>

            <template #footer>
                <button type="button"
                    class="btn btn-primary"
                    v-on:click="toggleModal()">
                    Close
                </button>
            </template>
        </ModalComponent>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useServiceStore } from '@/store';

import { DrawerChoices, ImageChoices } from '@/helpers/qr-generator.enum';
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
        const qrForm = ref({
            url: null,
            imageType: ImageChoices.PNG,
            frontColor: '#000000',
            backColor: '#ffffff',
            drawer: DrawerChoices.SQUAREM
        })
        const validation = {
            url: { 
                required: helpers.withMessage(
                    'Need to have a value',
                    required
                ),
                url: helpers.withMessage(
                    'Need to have a valid url',
                    url
                )}
        }
        const v$ = useVuelidate(validation, qrForm)

        // Checkers
        const isLoading = ref<boolean>(false)

        // Components
        const modalComponent = ref<InstanceType<typeof ModalComponent>>()

        // Generate QR
        const generateQR = () => {
            isLoading.value = true

            return serviceSvc.generateQR(
                qrForm.value
            ).then(data => {
                generatedResult.value = data.result
                isLoading.value = false
            }).catch(() => {
                isLoading.value = false
            })
        }

        // Reset service
        const reset = () => {
            v$.value.$reset()
            qrForm.value.url = null
            generatedResult.value = null
        }

        // Download output
        const download = () => {
            const filetype_ = qrForm.value.imageType
            const source = `data:image/${filetype_};base64,${generatedResult.value}`
            const fileName = `qrcode_`
            const downloadLink = document.createElement('a')
            downloadLink.href = source
            downloadLink.download = `${fileName}.${filetype_}`
            downloadLink.click()
        }

        // Toggle modal
        const toggleModal = () => {
            modalComponent.value?.toggleModal()
        }

        // Select drawer
        const onSelectDrawer = (mode: DrawerChoices) => {
            qrForm.value.drawer = mode
        }

        return {
            generatedResult,
            qrForm,
            v$,
            isLoading,
            modalComponent,
            generateQR,
            reset,
            download,
            toggleModal,
            onSelectDrawer,
            ImageChoices,
            DrawerChoices
        }
    },
    components: {
        ModalComponent
    },
})
</script>

<style lang="scss" scoped>
.drawer-img {
    padding: 0.3rem;
}

.drawer-img.selected {
    padding: 0;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.15), 
                0 1px 1px rgba(0, 0, 0, 0.075), 0 0 0 0.25rem rgba(118, 78, 209, .5);
}
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
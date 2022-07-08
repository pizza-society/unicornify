<template>
    <div class="container">
        <div class="d-flex flex-row vh-min justify-content-center align-items-center row">
            <div class="col-sm-12 col-md-4 text-center">
                <h3 class="mb-0">
                    URL Shortener
                </h3>
                <p class="mb-4">
                    <small>
                        Shorten your URL in a blink!
                    </small>
                </p>

                <div>
                    <form class="needs-validation">
                        <div class="mb-3">
                            <label class="form-label">Enter URL</label>
                            <input class="form-control"
                                placeholder="Enter link to shorten"
                                v-model="shortenForm.url"
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

                    <button class="btn btn-primary text-center"
                        v-on:click="shorten()"
                        :disabled="isLoading || v$.$invalid">
                        <span v-if="!isLoading">
                            Shorten
                        </span>
                        <span v-else>
                            <i class="fa-solid fa-spinner fa-spin"></i>
                        </span>
                    </button>
                </div>

                <Transition>
                    <div class="text-center"
                        v-if="shortedURL" >
                        <hr class="my-5" />
                        <div class="input-group">
                            <input type="text"
                                disabled
                                class="form-control form-control-dark bg-dark text-bg-dark"
                                placeholder="Recipient's username"
                                v-model="shortedURL" />
                            <button id="clipboardBtn"
                                type="button"
                                class="btn btn-primary"
                                v-on:click="copyToClipboard()">
                                <i class="fa-solid"
                                    :class="{
                                        'fa-clipboard': !isCopied,
                                        'fa-clipboard-check': isCopied
                                    }">
                                </i>
                            </button>
                        </div>
                    </div>
                </Transition>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useServiceStore } from '@/store';

import useVuelidate from '@vuelidate/core';
import { helpers, required, url } from '@vuelidate/validators';

export default defineComponent({
    name: 'ShortenerView',
    setup() {

        // Data
        const shortedURL = ref<string | null>(null)

        // Services
        const serviceSvc = useServiceStore()
        // const tippySvc = tippy

        // Forms
        const shortenForm = ref({
            url: null
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
                )
            }
        }
        const v$ = useVuelidate(validation, shortenForm)

        // Checkers
        const isLoading = ref<boolean>(false)
        const isCopied = ref<boolean>(false)

        // Shorten URL
        const shorten = () => {
            isCopied.value = false
            isLoading.value = true

            return serviceSvc.shortenURL(
                shortenForm.value
            ).then(data => {
                shortedURL.value = data.resultUrl
                isLoading.value = false
            }).catch(() => {
                isLoading.value = false
            })
        }

        const copyToClipboard = () => {
            isCopied.value = true
            navigator.clipboard.writeText(shortedURL.value ? shortedURL.value : '')
        }

        return {
            shortedURL,
            shortenForm,
            v$,
            isLoading,
            isCopied,
            shorten,
            copyToClipboard
        }
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
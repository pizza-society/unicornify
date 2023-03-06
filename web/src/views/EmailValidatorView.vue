<template>
    <div class="container">
        <div
            class="d-flex flex-row vh-min justify-content-center align-items-center row">
            <div class="col-lg-12 col-md-4 text-center">
                <ErrorAlert v-if="error">
                    An Error has occured, please try again later ...
                </ErrorAlert>

                <h3 class="mb-0">
                    Disposable Email Validator
                </h3>

                <p class="mb-4">
                    <small>
                        Validate disposable email address in seconds !
                    </small>
                </p>

                <div class="mb-3">
                    <div v-if="!formSubmitted">
                        <div class="container-sm">
                            <form @submit="validateEmail()" v-on:submit.prevent>
                                <span v-if="!isValidEmail">
                                    <div class="alert alert-light" role="alert">
                                        Please enter a valid email address
                                    </div>
                                </span>

                                <div v-if="!formSubmitted">
                                    <label class="form-label">
                                        Enter An Email
                                    </label>

                                    <input
                                        type="email"
                                        class="form-control"
                                        placeholder="Email address"
                                        aria-label="Email address"
                                        aria-describedby="button-addon1"
                                        v-model="emailForm.email"
                                        required />

                                    <br />

                                    <button
                                        class="btn btn-outline-primary"
                                        type="submit"
                                        id="button-addon1">
                                        Verify
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>

                    <div
                        v-else-if="dataObtained && !disposedEmailResult!.disposable && disposedEmailResult!.format">
                        <div class="alert alert-success" role="alert">
                            The Email <b>"{{ emailForm.email }}"</b> is Valid and Not
                            Disposable
                        </div>
                    </div>

                    <div
                        v-else-if="dataObtained && disposedEmailResult!.disposable">
                        <div class="alert alert-danger" role="alert">
                            Warning, The Email <b>"{{ emailForm.email }}"</b> is a
                            Disposable Email
                        </div>
                    </div>

                    <div
                        v-else-if="dataObtained && !disposedEmailResult!.format">
                        <div class="alert alert-light" role="alert">
                            The Email <b>"{{ emailForm.email }}"</b> is not a Valid Email.
                        </div>
                    </div>

                    <div v-else>
                        <div class="spinner-border" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>

                    <br />

                    <button
                        v-if="dataObtained"
                        type="button"
                        class="btn btn-primary btn-lg"
                        @click="formSubmitted = false; dataObtained = false;">
                        Check again
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang='ts'>
import { defineComponent, ref } from 'vue';

import ErrorAlert from '@/components/ErrorHandlers/ErrorAlert.vue';
import { useServiceStore } from '@/store';
import type { DisposableEmailMeta } from '@/types/disposable-email-validator.models';

export default defineComponent({
    name: 'email-validator',
    setup() {

        // Data
        const disposedEmailResult = ref<DisposableEmailMeta | null>(null)

        // Services
        const serviceSvc = useServiceStore()

        //  Forms 
        const emailForm = ref({ email: '' })

        // Checkers
        const formSubmitted = ref(false)
        const dataObtained = ref(false)
        const error = ref(false)
        const isValidEmail = ref(true)

        // Validate Email
        const validateEmail = () => {
            if (!testEmail()) {
                isValidEmail.value = false
                sleep(3000).then(() => {
                    isValidEmail.value = true
                })
                return
            }
            formSubmitted.value = true
            return serviceSvc.validateDisposableEmail(
                emailForm.value
                ).then(data => {
                    disposedEmailResult.value= data.result
                    dataObtained.value = true
                })
                .catch(() => {
                    error.value = true
                })
        }


        const testEmail = () => {
            const regex = /^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/
            return regex.test(emailForm.value.email)
        }

        const sleep = (time: number) => {
            return new Promise(resolve => setTimeout(resolve, time))
        }

        return {
            emailForm,
            formSubmitted,
            dataObtained,
            disposedEmailResult,
            error,
            isValidEmail,
            validateEmail,
            testEmail
        }
    },
    components: { ErrorAlert }
});

</script>
<style lang="scss" scoped>
.container-sm {
    max-width: 25rem;
}

.container {
    max-width: 50rem;
}
</style>

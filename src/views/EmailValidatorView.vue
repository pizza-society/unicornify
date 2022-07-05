<template>
    <div class="container">
        <div
            class="d-flex flex-row vh-min justify-content-center align-items-center row"
        >
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
                                    <label class="form-label"
                                        >Enter An Email</label
                                    >
                                    <input
                                        type="email"
                                        class="form-control"
                                        placeholder="Email address"
                                        aria-label="Email address"
                                        aria-describedby="button-addon1"
                                        v-model="emailForm.email"
                                        required
                                    />
                                    <br />
                                    <button
                                        class="btn btn-outline-primary"
                                        type="submit"
                                        id="button-addon1"
                                    >
                                        Verify
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                    <div
                        v-else-if="
                            dataObtained &&
                                !disposedEmailResponse.disposable &&
                                disposedEmailResponse.format
                        "
                    >
                        <div class="alert alert-success" role="alert">
                            The Email <b>"{{ email }}"</b> is Valid and Not
                            Disposable
                        </div>
                    </div>
                    <div
                        v-else-if="
                            dataObtained && disposedEmailResponse.disposable
                        "
                    >
                        <div class="alert alert-danger" role="alert">
                            Warning, The Email <b>"{{ email }}"</b> is a
                            Disposable Email
                        </div>
                    </div>
                    <div
                        v-else-if="
                            dataObtained && !disposedEmailResponse.format
                        "
                    >
                        <div class="alert alert-light" role="alert">
                            The Email <b>"{{ email }}"</b> is not a Valid Email.
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
                        @click="$router.go(0)"
                    >
                        Check again
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import ErrorAlert from "@/components/ErrorHandlers/ErrorAlert.vue";
import { useServiceStore } from "@/store";
import { mapActions } from "pinia";

undefined;
export default defineComponent({
    name: "email-validator",
    data() {
        return {
            emailForm: { email: "" } as any,
            formSubmitted: false as boolean,
            dataObtained: false as boolean,
            disposedEmailResponse: {} as any,
            error: false as boolean,
            isValidEmail: true as boolean
        };
    },
    methods: {
        ...mapActions(useServiceStore, ["validateDisposableEmail"]),
        validateEmail() {
            if (!this.testEmail()) {
                // Validate email
                this.isValidEmail = false;
                this.sleep(3000).then(() => {
                    this.isValidEmail = true;
                });
                return;
            }
            this.formSubmitted = true;
            this.validateDisposableEmail(this.emailForm)
                .then(data => {
                    // console.log("Response", data);
                    this.disposedEmailResponse = data.result;
                    this.dataObtained = true;
                })
                .catch(() => {
                    this.error = true;
                });
        },
        testEmail() {
            const regex = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,20}$/;
            return regex.test(this.emailForm.email);
        },

        sleep(time: number) {
            return new Promise(resolve => setTimeout(resolve, time));
        }
    },
    computed: {
        email(): string {
            return this.emailForm.email + "!";
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

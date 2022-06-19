<template>
    <div class="container pt-5">
        <div
            class="d-flex flex-column justify-content-center align-items-center"
        >
            <ErrorAlert v-if="error">
                An Error has occured, please try again later ...
            </ErrorAlert>
            <h4>
                <b>Email Address Validator</b>
            </h4>
            <div>
                <div v-if="!formSubmitted">
                    <lottie-player
                        src="https://assets3.lottiefiles.com/packages/lf20_ebqz3ltq.json"
                        background="transparent"
                        speed="1"
                        style="width: 350px; height: 350px;"
                        loop
                        autoplay
                    />
                </div>
                <div
                    v-else-if=
                    "
                        dataObtained && !response.disposable && response.format
                    "
                >
                    <lottie-player
                        src="https://assets4.lottiefiles.com/private_files/lf30_jgkflosi.json"
                        background="transparent"
                        speed="1"
                        style="width: 350px; height: 350px;"
                        autoplay
                    />
                </div>
                <div v-else-if="dataObtained">
                    <lottie-player
                        src="https://assets1.lottiefiles.com/packages/lf20_bdnjxekx.json"
                        background="transparent"
                        speed="1"
                        style="width: 350px; height: 350px;"
                        autoplay
                    />
                </div>
                <div v-else>
                    <lottie-player
                        src="https://assets6.lottiefiles.com/packages/lf20_0rvn1y9l.json"
                        background="transparent"
                        speed="1"
                        style="width: 400px; height: 400px;"
                        loop
                        autoplay
                    />
                </div>
            </div>
            <div v-if="!formSubmitted">
                <span>
                    <h4>
                        Email Validator is A Simple Little Tool for Validating
                        and Detecting Real/Disposable and Temporary Email
                        Addresses.
                    </h4>
                    <div class="container-sm">
                        <form @submit="makeApiCall()" v-on:submit.prevent>
                            <div class="form-group">
                                <div
                                    v-if="!formSubmitted"
                                    class="input-group  justify-content-center mt-4"
                                >
                                    <input
                                        type="email"
                                        class="form-control-lg"
                                        placeholder="Email address"
                                        aria-label="Email address"
                                        aria-describedby="button-addon1"
                                        v-model="userEmail"
                                        required
                                    />
                                    <button
                                        class="btn btn-outline-primary"
                                        type="submit"
                                        id="button-addon1"
                                    >
                                        Verify
                                    </button>
                                </div>
                            </div>
                        </form>
                        <br />
                    </div>
                    <h5>
                        <b
                            >Add an email address above to verify its validity
                            in real - time basis.
                        </b>
                    </h5>
                </span>
            </div>
            <div
                v-else-if=
                "
                    dataObtained && !response.disposable && response.format
                "
            >
                <h2>
                    The Email <b>"{{ email }}"</b> is Valid and Not Disposable
                    😁.
                </h2>
            </div>
            <div v-else-if="dataObtained && response.disposable">
                <h4>
                    Warning, The Email <b>"{{ email }}"</b> is a Disposable
                    Email.
                </h4>
            </div>
            <div v-else-if="dataObtained && !response.format">
                <h4>
                    Warning, The Email <b>"{{ email }}"</b> is not a Valid
                    Email.
                </h4>
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
</template>

<script lang="ts">
import { defineComponent } from "vue";
import ErrorAlert from "@/components/ErrorHandlers/ErrorAlert.vue";
import axios from "axios";
import ResponseData from "../types/ResponseData";
undefined;
export default defineComponent({
    name: "email-validator",
    data() {
        return {
            userEmail: "" as string,
            formSubmitted: false as boolean,
            dataObtained: false as boolean,
            response: "" as any,
            error: false as boolean
        };
    },
    methods: {
        makeApiCall() {
            this.formSubmitted = true;
            axios
                .get(`https://www.disify.com/api/email/${this.userEmail}`)
                .then((response: ResponseData) => {
                    // console.log("Response", response.data);
                    this.response = response.data;
                    this.sleep(3000).then(() => {
                        this.dataObtained = true;
                    });
                })
                .catch(err => {
                    console.log("Error", err);
                    this.error = true;
                    setTimeout(() => this.$router.push({ name: "home" }), 5000);
                });
        },
        sleep(time: number) {
            return new Promise(resolve => setTimeout(resolve, time));
        }
    },
    computed: {
        email(): string {
            return this.userEmail + "!";
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

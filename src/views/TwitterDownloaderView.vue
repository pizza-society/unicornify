<template>
    <div class="container">
        <div
            class="d-flex flex-column justify-content-center align-items-center"
        >
            <lottie-player
                src="https://assets2.lottiefiles.com/private_files/lf30_pdS85G.json"
                background="transparent"
                speed="0.5"
                style="width: 300px; height: 300px;"
                loop
                autoplay
            />
            <div class="col-lg-6 col-md-4 text-center">
                <figure class="text-center">
                    <blockquote class="blockquote">
                        <h3 class="mb-4">
                            Twitter Video Downloader
                        </h3>
                    </blockquote>
                    <figcaption class="blockquote-footer">
                        Download Twitter Videos in seconds...
                    </figcaption>
                </figure>
                <div class="mb-3">
                    <form v-on:submit.prevent class="needs-validation">
                        <div class="row rounded-top ">
                            <div class="input-group">
                                <div class="input-group mb-3">
                                    <input
                                        type="text"
                                        class="form-control form-control-lg"
                                        placeholder="Enter Video Link..."
                                        aria-label="Enter Video Link..."
                                        aria-describedby="button-addon2"
                                        v-model="downloadForm.url"
                                        :disabled="isLoading"
                                        @blur="v$.url.$touch"
                                        :class="{
                                            'is-invalid':
                                                v$.url.$error && v$.url.$dirty,
                                            'is-valid':
                                                !v$.url.$error && v$.url.$dirty
                                        }"
                                    />
                                    <div
                                        class="invalid-feedback"
                                        v-for="error of v$.url.$errors"
                                        :key="error.$uid"
                                    >
                                        {{ error.$message }}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </form>
                    <button
                        class="btn btn-primary"
                        type="button"
                        id="button-addon2"
                        v-on:click="getTweetMedia()"
                        :disabled="isLoading || v$.$invalid"
                    >
                        >
                        <span v-if="!isLoading">
                            Download
                        </span>
                        <span v-else>
                            <span
                                class="spinner-grow spinner-grow-sm"
                                role="status"
                                aria-hidden="true"
                            />
                            Loading...
                        </span>
                    </button>

                    <figure class="text-center mt-4">
                        <figcaption class="blockquote-footer">
                            Link example:
                            https://twitter.com/unicornify/status/882987478541533189
                        </figcaption>
                    </figure>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { useServiceStore } from "@/store";
import { defineComponent, ref } from "vue";
import useVuelidate from "@vuelidate/core";
import { helpers, required } from "@vuelidate/validators";
export default defineComponent({
    name: "TwitterDownloaderView",
    setup() {
        // Data
        const generatedResult = ref<object | null | unknown>(null);

        // Services
        const serviceSvc = useServiceStore();

        // Form
        const downloadForm = ref({
            url: null,
            quality: null
        });

        // Twitter Status regex: https://stackoverflow.com/a/4138539/16711156
        const twitterStatusRegex = helpers.regex(
            /^https?:\/\/twitter\.com\/(?:#!\/)?(\w+)\/status(?:es)?\/(\d+)(?:\/.*)?$/
        );
        //  declare our validation rules with validations validation rules.
        const validation = {
            url: {
                required: helpers.withMessage(
                    "Please fill this field",
                    required
                ),
                url: helpers.withMessage(
                    "Please enter a valid twitter status link",
                    twitterStatusRegex
                )
            }
        };

        // activate Vuelidate inside setup by calling useVuelidate.
        const v$ = useVuelidate(validation, downloadForm); // useVuelidate(rules, state), v$ Vuelidate object.

        // Checkers
        const isLoading = ref<boolean>(false);

        // Get resolutions
        const getTweetMedia = () => {
            isLoading.value = true;
            console.log("downloadForm.value.url", downloadForm.value.url);
        };
        return { generatedResult, downloadForm, v$, isLoading, getTweetMedia };
    },
    components: {}
});
</script>

<style lang="scss"></style>

<template>
    <div class="container">
        <div
            class="d-flex flex-column justify-content-center align-items-center">
            <lottie-player
                src="https://assets2.lottiefiles.com/private_files/lf30_pdS85G.json"
                background="transparent"
                speed="0.5"
                style="width: 300px; height: 300px;"
                loop
                autoplay/>

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

				<ErrorAlert v-if="error">
					The twitter link you supplied does not include any video 
                    or that there is a problem downloading the video.
				</ErrorAlert> 

                <div class="mb-3">
                    <div v-if="tweetMedias && tweetMetaData && !isLoading && !error">
                        <div class="card text-center text-bg-dark mb-3">
                            <div class="card-header">
                                <h5 class="card-title">
                                    {{ tweetMetaData.uploader_display_name }}
                                </h5>
                            </div>

                            <div class="card-body">
                                <!-- <h5 class="card-title">{{tweetMetaData.uploader_display_name}}</h5> -->
                                <p class="card-text">
                                    {{ tweetMetaData.description }}
                                </p>
                            </div>

                            <div class="card-footer text-muted">
                                <div class="row g-0 text-bg-dark ">
                                    <div class="col-md-4 img-container">
                                        <img
                                            :src="tweetMetaData.thumbnail"
                                            class="img-fluid rounded-start"/>
                                    </div>

                                    <div class="col-md-8">
                                        <div class="card-body">
                                            <!-- <h5 class="card-title">Card title</h5> -->
                                            <!-- <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p> -->
                                            <div class="card-text">
                                                <table
                                                    class="table table-dark table-hover">
                                                    <thead>
                                                        <tr>
                                                            <th scope="col">
                                                                Quality
                                                            </th>

                                                            <th scope="col">
                                                                Downloads
                                                            </th>
                                                        </tr>
                                                    </thead>

                                                    <tbody>
                                                        <tr
                                                            v-for="value in tweetMedias"
                                                            :key="value">
                                                            <td>
                                                                {{value.resolution}}
                                                            </td>

                                                            <td>
                                                                <a  @click="downloadVideo(value.url)">
                                                                    Download
                                                                </a>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                    
                                                </table>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <form @submit.prevent class="needs-validation">
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
                                            'is-invalid': v$.url.$error && v$.url.$dirty,
                                            'is-valid': !v$.url.$error && v$.url.$dirty
                                        }"/>

                                    <div
                                        class="invalid-feedback"
                                        v-for="error of v$.url.$errors"
                                        :key="error.$uid">
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
                        @click="getTweetMedia()"
                        :disabled="isLoading || v$.$invalid">
                        <span v-if="!isLoading">
                            Download
                        </span>

                        <span v-else>
                            <span
                                class="spinner-grow spinner-grow-sm"
                                role="status"
                                aria-hidden="true"/>
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
import { defineComponent, ref } from "vue";

import useVuelidate from '@vuelidate/core';
import { helpers, or, required } from '@vuelidate/validators';

import { useServiceStore } from '@/store';
import ErrorAlert from '@/components/ErrorHandlers/ErrorAlert.vue';

export default defineComponent({
    name: 'TwitterDownloaderView',
    setup() {

        // Data
        const tweetMetaData = ref<any>(null)
        const tweetMedias = ref<any>(null)
        const error = ref<boolean>(false)

        // Services
        const serviceSvc = useServiceStore()

        // Form
        const downloadForm = ref({
            url: null
        })

        // Twitter Status Regex
        // I.e:  https://twitter.com/TheOceanCleanup/status/1551568161018871810
        const twRegexNormalStatus = helpers.regex(
            /^https?:\/\/twitter\.com\/(?:#!\/)?(\w+)\/status(?:es)?\/(\d+)(?:\/.*)?$/
        )
        // I.e: https://mobile.twitter.com/TheOceanCleanup/status/1551568161018871810
        const twRegexMobileBrowserStatus = helpers.regex(
            /^https?:\/\/(?:mobile.)?twitter\.com\/(?:#!\/)?(\w+)\/status(?:es)?\/(\d+)(?:\/.*)?$/
        )
        // I.e: https://twitter.com/tansuyegen/status/1553643510271807489?s=24&t=DWBlw1gZk3FFWVQYOHUGYw
        const twRegexMobileShareStatus = helpers.regex(
            /^https?:\/\/(?:mobile.)?twitter\.com\/(?:#!\/)?(\w+)\/status(?:es)?\/(\d+)(?:\/.*)?((\?)(.+))?$/
        )

        const validation = {
            url: {
                required: helpers.withMessage(
                    'Please fill this field',
                    required
                ),
                url: helpers.withMessage(
                    'Please enter a valid twitter status link',
                    or(
                        twRegexNormalStatus,
                        twRegexMobileBrowserStatus,
                        twRegexMobileShareStatus
                    )
                )
            }
        }

        const v$ = useVuelidate(validation, downloadForm)

        // Checkers
        const isLoading = ref<boolean>(false)

        // Get resolutions
        const getTweetMedia = () => {
            isLoading.value = true
            tweetMedias.value = null
            tweetMetaData.value = null
            return serviceSvc
                .downloadTwitterVideo(downloadForm.value)
                .then(data => {
                    if(data.result.error) throw new Error("There's no video in this tweet")
                    // Tweet media file data
                    tweetMedias.value = data.result.tweet_medias
                    // Tweet meta file data
                    tweetMetaData.value = data.result.tweet_meta_data
                    isLoading.value = false
                })
                .catch(() => {
                    tweetMedias.value = null
                    tweetMetaData.value = null
                    isLoading.value = false
                    displayErrorMessage(5000)   
                })
        }

        // Error Handler
		const displayErrorMessage = (duration: number) => {
			error.value = true
			sleep(duration).then(() => {
				error.value = false
			})
        }
        
        const sleep = (time: number) => {
			return new Promise(resolve => setTimeout(resolve, time))
		}

        // Download tweet video
        const downloadVideo = (url: string) => {
            serviceSvc.downloadBlobFile(url, 'video/mp4', 'tweet-video')
        }

        return {
            downloadForm,
            v$,
            isLoading,
            tweetMedias,
            tweetMetaData,
            error,
            getTweetMedia,
            downloadVideo,
            displayErrorMessage
        }
    },
    components: { ErrorAlert }
})
</script>

<style lang="scss" scoped>
.img-container  {
    height: 200px;
    width: 200px;
}


.img-container img {
    max-height: 100%;
}
</style>

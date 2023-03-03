<template>
  <div class="container">
      <div
          class="d-flex flex-column justify-content-center align-items-center">
          <lottie-player
            v-if="!TikTokMediaData"
              src="https://assets7.lottiefiles.com/packages/lf20_5h2kp8uz.json"
              background="transparent"
              speed="0.5"
              style="width: 300px; height: 300px;"
              loop
              autoplay/>

            
            <div class="col-lg-8 text-center">
                    <figure 
                        v-if="!TikTokMediaData && !error"
                        class="text-center">

                        <blockquote class="blockquote">
                            <h3 class="mb-4">
                                TikTok Downloader
                            </h3>
                        </blockquote>

                        <figcaption class="blockquote-footer">
                            Download TikTok Videos in seconds...
                        </figcaption>

                    </figure>

                    <ErrorAlert v-if="error">
                        The TikTok link you supplied does not include any video 
                        or that there is a problem downloading the video.
                    </ErrorAlert>

                    <Transition>
                        <div 
                            v-if="TikTokMediaData && tikTokMetaData && !isLoading && !error">
                                <div class="card text-bg-dark mb-3 mt-5" >
                                    <div class="row g-0">

                                        <div class="col-md-4">
                                            <img :src="tikTokMetaData.thumbnail" class="img-fluid rounded-start">
                                        </div>

                                        <div class="col-md-8">
                                            <div class="card-header">
                                                <h5 class="card-title">
                                                    <i class="fa-solid fa-user"></i>
                                                    {{ tikTokMetaData.creator }}
                                                </h5>
                                            </div>

                                            <div class="card-body">
                                                <p class="card-text">
                                                    {{ tikTokMetaData.description }}
                                                </p>
                                            </div>

                                            <div class="card-body">
                                                <ul class="list-group list-group-flush">
                                                    <li 
                                                        class="list-group-item thumbnail"                                                              
                                                        v-for="(item, index) in TikTokMediaData"
                                                        :key="index"
                                                        @click="downloadVideo(item.url)">
                                                        <i class="fa-solid fa-circle-arrow-down"></i>
                                                        <span>
                                                            Download {{ item.format_note }} [{{ Number(index) + 1 }}]
                                                        </span>
                                                    </li>
                                                </ul>
                                            </div>
                                            
                                            <div class="card-footer">
                                                <i class="fa-solid fa-video"></i>
                                                {{ convertToTime(tikTokMetaData.duration_string) }}
                                            </div>

                                        </div>

                                    </div>
                                    
                                </div>

                        </div>

                    </Transition>
            </div>
              <!-- Form -->
            <div class="col-lg-6 text-center">                  
                <form @submit.prevent class="needs-validation">
                    <div class="row rounded-top">
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
                    @click="getTikTokMedia()"
                    :disabled="isLoading || v$.$invalid">
                    <span v-if="!isLoading">
                        Download
                    </span>

                    <span v-else>

                        <span
                            class="spinner-grow spinner-grow-sm"
                            role="status"
                            aria-hidden="true">
                        </span>
                            Loading...
                    </span>
                </button>

                <figure class="text-center mt-4">
                    <figcaption class="blockquote-footer">
                        Link example:
                        https://www.tiktok.com/@unicornify/video/0123456789
                    </figcaption>
                </figure>
                
            </div>
      </div>
  </div>
</template>




<script lang="ts">
import { useServiceStore } from "@/store";
import { defineComponent, ref } from "vue";

import useVuelidate from "@vuelidate/core";
import { tikTokLinkRegex, convertToTime, sleep } from "@/helpers/helpers";
import { helpers, or, required } from "@vuelidate/validators";
import ErrorAlert from "@/components/ErrorHandlers/ErrorAlert.vue";
import { TikTokMedia, TikTokMeta } from "@/types/tiktok-downloader.model";

export default defineComponent({
    name: "TikTokDownloaderView",
    setup() {
        

        // Data
        const tikTokMetaData = ref<TikTokMeta | null>()
        const TikTokMediaData = ref<TikTokMedia[] | null>()

        let error = ref<boolean>(false)

        // Services
        const serviceSvc = useServiceStore()

        // Form
        const downloadForm = ref({
            url: null
        })

        const validation = {
            url: {
                required: helpers.withMessage(
                    "Please fill this field",
                    required
                ),
                url: helpers.withMessage(
                    "Please enter a valid TikTok link",
                    or(
                        tikTokLinkRegex
                    )
                )
            }
        }

        const v$ = useVuelidate(validation, downloadForm)

        // Checkers
        const isLoading = ref<boolean>(false)

        // Get resolutions
        const getTikTokMedia = () => {
            isLoading.value = true
            TikTokMediaData.value = null
            tikTokMetaData.value = null
            return serviceSvc
                .downloadTikTokVideo(downloadForm.value)
                .then(data => {
                    if (data.result.error) throw new Error("There's no video in this link")
                    // TikTok media file data
                    TikTokMediaData.value = data.result.medias
                    // TiKTok meta file data
                    tikTokMetaData.value = data.result
                    isLoading.value = false
                })
                .catch(() => {
                    TikTokMediaData.value = null
                    tikTokMetaData.value = null
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


        // Download Tiktok video
        const downloadVideo = (url: string) => {
            serviceSvc.downloadBlobFile(url, "video/mp4", "tiktok-video", true, { url: url })
        }

        return {
            downloadForm,
            v$,
            isLoading,
            TikTokMediaData,
            tikTokMetaData,
            error,
            getTikTokMedia,
            downloadVideo,
            displayErrorMessage,
            convertToTime
        }
    },
    components: { ErrorAlert }
})
</script>
<style lang="scss" scoped>


.v-enter-active,
.v-leave-active {
  transition: all .2s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}

.v-enter-from {
  transform: translateY(10px);
  opacity: 0;
}

.v-leave-to {
  transform: translateY(100px);
  opacity: 0;
}

.thumbnail:hover {
opacity: 0.5;
}

.list-group-item {
    cursor: pointer;
}

@media only screen and (max-width: 767px) {
    .img-fluid {
      height: 350px;
    }
  }

</style>
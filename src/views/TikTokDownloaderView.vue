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
              <!-- Form -->
              <div class="mb-3">
                  <Transition>
                      <div v-if="tikTokMediasData && tikTokMetaData && !isLoading && !error">
                          <div class="card text-center text-bg-dark mb-3">
                              <div class="card-header">
                                  <h5 class="card-title">
                                      {{ tikTokMetaData.creator }}
                                  </h5>
                              </div>
                              <div class="card-body">
                                  <!-- <h5 class="card-title">{{tweetMetaData.uploader_display_name}}</h5> -->
                                  <p class="card-text">
                                      {{ tikTokMetaData.description }}
                                  </p>
                              </div>
                              <div class="card-footer text-muted">
                                  <div class="row g-0 text-bg-dark ">
                                      <div class="img-container">
                                          <img
                                              :src="tikTokMetaData.thumbnail"
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
                                                              v-for="value in tikTokMediasData"
                                                              :key="value"
                                                              style="cursor: pointer;"
                                                              @click="downloadVideo(value.url)"
                                                              >
                                                              <td>
                                                                  {{value.resolution}}
                                                              </td>
                                                              <td>
                                                                  Download
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
                  </Transition>
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
                      aria-hidden="true"/>
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
  </div>
</template>




<script lang="ts">
import { useServiceStore } from "@/store";
import { defineComponent, ref } from "vue";

import useVuelidate from "@vuelidate/core";

import { helpers, or, required } from "@vuelidate/validators";
import ErrorAlert from "@/components/ErrorHandlers/ErrorAlert.vue";
import { TikTokMedias, TikTokMeta } from "@/types/tiktok-downloader.model";

export default defineComponent({
  name: "TikTokDownloaderView",
  setup() {

      // Data
      const tikTokMetaData = ref<TikTokMeta | null>();
      const tikTokMediasData = ref<TikTokMedias | any>();

      let error = ref<boolean>(false)

      // Services
      const serviceSvc = useServiceStore();

      // Form
      const downloadForm = ref({
          url: null
      });
      /*
      -  Tiktok Link Regex
        https://stackoverflow.com/questions/74077377/regular-expression-to-match-any-tiktok-video-id-and-url
       I.e: 
          - https://m.tiktok.com/h5/share/usr/6641141594707361797.html
          - https://m.tiktok.com/v/6749869095467945218.html
          - https://www.tiktok.com/embed/6567659045795758085
          - https://www.tiktok.com/share/user/6567659045795758085
          - https://www.tiktok.com/trending?shareId=6744531482393545985
          - https://www.tiktok.com/@burntpizza89/video/7067695578729221378?is_copy_url=1&is_from_webapp=v1
          - https://www.tiktok.com/@burntpizza89/video/is_copy_url=1&is_from_webapp=v1&item_id=7067695578729221378
          - https://vm.tiktok.com/ZMF6rgvXY/
      */

      const tikTokLinkRegex = helpers.regex(
        // eslint-disable-next-line no-useless-escape
        /\bhttps?:\/\/(?:m|www|vm)\.tiktok\.com\/(?:.*\b(?:(?:usr|v|embed|user|video)\/|\?shareId=|\&item_id=)(\d+)\b|([\w\d]+))/gm
      );

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
      };

      const v$ = useVuelidate(validation, downloadForm);

      // Checkers
      const isLoading = ref<boolean>(false);

      // Get resolutions
      const getTikTokMedia = () => {
          isLoading.value = true;
          tikTokMediasData.value = null;
          tikTokMetaData.value = null;
          return serviceSvc
              .downloadTikTokVideo(downloadForm.value)
              .then(data => {
                  if(data.result.error) throw new Error("There's no video in this link");
                  // TikTok media file data
                  tikTokMediasData.value = data.result.medias;
                  // TiKTok meta file data
                  tikTokMetaData.value = data.result;
                  isLoading.value = false;
              })
              .catch(() => {
                  tikTokMediasData.value = null;
                  tikTokMetaData.value = null;
                  isLoading.value = false;
                  displayErrorMessage(5000)   
              });
      };

      // Error Handler
  const displayErrorMessage = (duration: number) => {
    error.value = true;
    sleep(duration).then(() => {
      error.value = false;
    });
      }
      
      const sleep = (time: number) => {
    return new Promise(resolve => setTimeout(resolve, time));
  }

      // Download Tiktok video
      const downloadVideo = (url: string) => {
          console.log(url)
          serviceSvc.downloadBlobFile(url, "video/mp4", "tiktok-video");
      };

      return {
          downloadForm,
          v$,
          isLoading,
          tikTokMediasData,
          tikTokMetaData,
          error,
          getTikTokMedia,
          downloadVideo,
          displayErrorMessage
      };
  },
  components: { ErrorAlert }
});
</script>
<style lang="scss" scoped>
.img-container {
  height: 200px;
  width: 200px;
}


.img-container img {
  max-height: 100%;
}

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
  transform: translateY(10px);
  opacity: 0;
}

.v-leave-to {
  transform: translateY(10px);
  opacity: 0;
}
</style>
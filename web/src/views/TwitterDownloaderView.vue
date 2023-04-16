<template>
	<div class="container">
		<div class="d-flex flex-column justify-content-center align-items-center">
			<div class="col-sm-12 col-md-4 text-center">
				<div class="header-container">
					<lottie-player
						src="https://assets2.lottiefiles.com/private_files/lf30_pdS85G.json"
						background="transparent"
						class="mx-auto"
						speed="1"
						style="width: 15rem; height: 15rem;"
						autoplay />
				</div>

				<figure 
					v-if="!tweetMetaData && !formError"
					class="text-center">
					<blockquote class="blockquote">
						<h3 class="mb-4">
							Twitter Video Downloader
						</h3>
					</blockquote>

					<figcaption class="blockquote-footer">
						Download Twitter Videos in seconds...
					</figcaption>
				</figure>

				<ErrorAlert v-if="formError">
					The twitter link you supplied does not include any video 
					or that there is a problem downloading the video.
				</ErrorAlert>
				
				<Transition>
					<div v-if="tweetMedias && tweetMetaData && !isLoading && !formError">
						<div class="card text-bg-dark mb-3 mt-5">
							<div class="row g-0">
								<div class="col-md-4">
									<img
										class="img-fluid rounded-start"
										:src="tweetMetaData.thumbnail" />
								</div>

								<div class="col-md-8">
									<div class="card-header">
										<h5 class="card-title">
											<i class="fa-solid fa-user"></i>
											{{ tweetMetaData.uploaderDisplayName }}
										</h5>
									</div>

									<div class="card-body">
										<p class="card-text">
											{{ tweetMetaData.description }}
										</p>
									</div>

									<div class="card-body">
										<ul>
											<li
												v-for="(item, index) in tweetMedias"
												:key="index"   
												type="button"                                                           
												class="list-group-item thumbnail m-2 p-2 bg-primary rounded"
												@click="downloadVideo(item.url)">
												<i class="fa-solid fa-circle-arrow-down"></i>

												<span>
													Download {{ item.resolution }} [{{ Number(index) + 1 }}]
												</span>
											</li>
										</ul>
									</div>
                                    
									<div class="card-footer">
										<i class="fa-solid fa-video"></i>
										{{ tweetMetaData.duration }}
									</div>
								</div>
							</div>
						</div>
					</div>
				</Transition>
				
				<div class="mb-3">
					<!-- Form -->
					<form
						class="needs-validation"
						@submit.prevent>
						<div class="row rounded-top ">
							<label class="form-label text-center">
								Enter URL
							</label>
							
							<div class="input-group">
								<div class="input-group mb-3">
									<TheInput
										v-model="downloadForm.url"
										type="text"
										placeholder="Enter Video Link..."
										:disabled="isLoading"
										:class="{
											'is-invalid': v$.url.$error && v$.url.$dirty,
											'is-valid': !v$.url.$error && v$.url.$dirty
										}"
										@blur="v$.url.$touch" />
										
									<div
										v-for="error of v$.url.$errors"
										:key="error.$uid"
										class="invalid-feedback">
										{{ error.$message }}
									</div>
								</div>
							</div>
						</div>
					</form>

					<button
						class="btn btn-primary"
						:disabled="isLoading || v$.$invalid"
						@click="getTweetMedia()">
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
							https://twitter.com/unicornify/status/882987478541533189
						</figcaption>
					</figure>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useServiceStore } from '@/store'

import useVuelidate from '@vuelidate/core'
import { helpers, required } from '@vuelidate/validators'

import { TweetMedia, TweetMeta } from '@/types/twitter-downloader.model'
import { sleep } from '@/helpers/timer'
import { twitterStatusRegex } from '@/helpers/regex'
import ErrorAlert from '@/components/ErrorHandlers/ErrorAlert.vue'
import TheInput from '@/components/forms/TheInput.vue'

export default defineComponent({
	name: 'TwitterDownloaderView',
	components: { ErrorAlert, TheInput },
	setup() {
		// Data
		const tweetMetaData = ref<TweetMeta | null>(null)
		const tweetMedias = ref<TweetMedia[] | null>(null)
		const formError = ref<boolean>(false)

		// Services
		const serviceSvc = useServiceStore()

		// Form
		const downloadForm = ref({
			url: null
		})

		const validation = {
			url: {
				required: helpers.withMessage(
					'Please fill this field',
					required
				),
				url: helpers.withMessage(
					'Please enter a valid twitter status link',
					twitterStatusRegex
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
					if(data.result.error) {
						throw new Error('There\'s no video in this tweet')
					}

					// Tweet media file data
					tweetMedias.value = data.result.tweetMedias
					// Tweet meta file data
					tweetMetaData.value = data.result.tweetMetaData
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
			formError.value = true
			sleep(duration).then(() => {
				formError.value = false
			})
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
			formError,
			getTweetMedia,
			downloadVideo,
			displayErrorMessage
		}
	}
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

@media only screen and (max-width: 767px) {
    .img-fluid {
        height: 350px;
    }
}

.header-container {
	padding-top: 0.5rem;
	padding-bottom: 0.5rem;
}
</style>

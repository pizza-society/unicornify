<template>
	<div class="container">
		<div class="d-flex flex-column justify-content-center align-items-center">
			<div class="col-sm-12 col-md-4 text-center">
				<div class="header-container">
					<lottie-player
						v-if="!tikTokMediaData"
						src="https://assets7.lottiefiles.com/packages/lf20_5h2kp8uz.json"
						background="transparent"
						class="mx-auto"
						speed="1"
						style="width: 15rem; height: 15rem;"
						autoplay />
				</div>

				<div class="text-center">
					<div 
						v-if="!tikTokMediaData && !formError"
						class="text-center">
						<h3 class="mb-0">
							TikTok Downloader
						</h3>

						<p class="mb-4 text-secondary">
							<small>
								Download TikTok Videos in seconds...
							</small>
						</p>
					</div>

					<ErrorAlert v-if="formError">
						The TikTok link you supplied does not include any video 
						or that there is a problem downloading the video.
					</ErrorAlert>
		
					<Transition>
						<div v-if="tikTokMediaData && tikTokMetaData && !isLoading && !formError">
							<div class="card text-bg-dark mb-3 mt-5">
								<div class="row g-0">
									<div class="col-md-4">
										<img
											class="img-fluid rounded-start"
											:src="tikTokMetaData.thumbnail" />
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
											<ul>
												<li
													v-for="(item, index) in tikTokMediaData"
													:key="index"   
													type="button"     
													class="list-group-item thumbnail m-2 p-2 bg-primary rounded"
													@click="downloadVideo(item.url)">
													<i class="fa-solid fa-circle-arrow-down mx-2"></i>

													<span>
														{{ item.resolution }} [{{ Number(index) + 1 }}]
													</span>
												</li>
											</ul>
										</div>
                                    
										<div class="card-footer">
											<i class="fa-solid fa-video"></i>
											{{ convertToTime(tikTokMetaData.durationString) }}
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
							<div class="row rounded-top">
								<label class="form-label text-center">
									Enter URL
								</label>

								<div class="input-group mb-3">
									<TheInput 
										v-model="downloadForm.url"
										type="text"
										placeholder="Enter link (Eg: https://tiktok.com/@user/video/1234)"
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
						</form>

						<button
							class="btn btn-primary"
							type="button"
							:disabled="isLoading || v$.$invalid"
							@click="getTikTokMedia()">
							<span v-if="!isLoading">
								Download
							</span>

							<span v-else>
								<i class="fa-solid fa-spinner fa-spin"></i>
								Loading...
							</span>
						</button>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

import useVuelidate from '@vuelidate/core'
import { helpers, required } from '@vuelidate/validators'

import ErrorAlert from '@/components/ErrorHandlers/ErrorAlert.vue'
import TheInput from '@/components/forms/TheInput.vue'
import { useServiceStore } from '@/store'
import { convertToTime, sleep } from '@/helpers/timer'
import { tikTokLinkRegex } from '@/helpers/regex'
import type { TikTokMedia, TikTokMeta } from '@/types/tiktok-downloader.model'

export default defineComponent({
	name: 'TikTokDownloaderView',
	components: {
		ErrorAlert,
		TheInput
	},
	setup() {
		// Data
		const tikTokMetaData = ref<TikTokMeta | null>()
		const tikTokMediaData = ref<TikTokMedia[] | null>()
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
					'Please enter a valid TikTok link',
					tikTokLinkRegex
				)
			}
		}
		const v$ = useVuelidate(validation, downloadForm)

		// Checkers
		const isLoading = ref<boolean>(false)

		// Get resolutions
		const getTikTokMedia = () => {
			isLoading.value = true
			tikTokMediaData.value = null
			tikTokMetaData.value = null
			return serviceSvc
				.downloadTikTokVideo(downloadForm.value)
				.then(data => {
					if (data.result.error) {
						throw new Error('There\'s no video in this link')
					}

					// TikTok media file data
					tikTokMediaData.value = data.result.medias
					// TiKTok meta file data
					tikTokMetaData.value = data.result
					isLoading.value = false
				})
				.catch(() => {
					tikTokMediaData.value = null
					tikTokMetaData.value = null
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

		// Download Tiktok video
		const downloadVideo = (url: string) => {
			serviceSvc.downloadBlobFile(url, 'video/mp4', 'tiktok-video', true, { url: url })
		}

		return {
			downloadForm,
			v$,
			isLoading,
			tikTokMediaData,
			tikTokMetaData,
			formError,
			getTikTokMedia,
			downloadVideo,
			displayErrorMessage,
			convertToTime
		}
	}
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

@media only screen and (max-width: 767px) {
    .img-fluid {
        height: 350px;
    }
}
</style>
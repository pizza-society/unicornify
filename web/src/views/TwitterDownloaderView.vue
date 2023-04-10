<template>
	<div class="container">
		<div
			class="d-flex flex-column justify-content-center
            align-items-center">
			<lottie-player
				src="https://assets2.lottiefiles.com/private_files/lf30_pdS85G.json"
				background="transparent"
				speed="0.5"
				style="width: 300px; height: 300px;"
				loop
				autoplay />

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
									{{ tweetMetaData.uploaderDisplayName }}
								</h5>
							</div>

							<div class="card-body">
								<p class="card-text">
									{{ tweetMetaData.description }}
								</p>
							</div>

							<div class="card-footer text-muted">
								<div class="row g-0 text-bg-dark ">
									<div class="col-md-4 img-container">
										<img
											:src="tweetMetaData.thumbnail"
											class="img-fluid rounded-start" />
									</div>

									<div class="col-md-8">
										<div class="card-body">
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
															v-for="(item, index) in tweetMedias"
															:key="index">
															<td>
																{{ item.resolution }}
															</td>

															<td>
																<a @click="downloadVideo(item.url)">
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

					<form
						class="needs-validation"
						@submit.prevent>
						<div class="row rounded-top ">
							<div class="input-group">
								<div class="input-group mb-3">
									<input
										v-model="downloadForm.url"
										type="text"
										class="form-control form-control-lg"
										placeholder="Enter Video Link..."
										aria-label="Enter Video Link..."
										aria-describedby="button-addon2"
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
						id="button-addon2"
						class="btn btn-primary"
						type="button"
						:disabled="isLoading || v$.$invalid"
						@click="getTweetMedia()">
						<span v-if="!isLoading">
							Download
						</span>

						<span v-else>
							<span
								class="spinner-grow spinner-grow-sm"
								role="status"
								aria-hidden="true"></span>
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

import useVuelidate from '@vuelidate/core'
import { helpers, required } from '@vuelidate/validators'

import { useServiceStore } from '@/store'
import { twitterStatusRegex, sleep } from '@/helpers/helpers'
import ErrorAlert from '@/components/ErrorHandlers/ErrorAlert.vue'
import { TweetMedia, TweetMeta } from '@/types/twitter-downloader.model'

export default defineComponent({
	name: 'TwitterDownloaderView',
	components: { ErrorAlert },
	setup() {
		// Data
		const tweetMetaData = ref<TweetMeta | null>(null)
		const tweetMedias = ref<TweetMedia[] | null>(null)
		const error = ref<boolean>(false)

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
			error.value = true
			sleep(duration).then(() => {
				error.value = false
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
			error,
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
</style>

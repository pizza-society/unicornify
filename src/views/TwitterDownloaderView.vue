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
					<form v-on:submit.prevent>
						<div class="row rounded-top ">
							<div class="input-group">
								<div class="input-group mb-3">
									<input
										type="text"
										class="form-control form-control-lg"
										placeholder="Enter Video Link..."
										aria-label="Enter Video Link..."
										aria-describedby="button-addon2"
									/>
									<button
										class="btn btn-primary"
										type="button"
										id="button-addon2"
									>
										Download
									</button>
								</div>
							</div>
						</div>
					</form>
					<figure class="text-center mt-3">
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
import { defineComponent } from "vue";

export default defineComponent({
	name: "TwitterDownloaderView",
	setup() {
		return {};
	},
	components: {}
});
</script>

<style lang="scss"></style>

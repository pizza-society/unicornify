<template>
	<div class="container">
		<div class="d-flex flex-row vh-min justify-content-center row">
			<div class="col-sm-12 col-md-4 text-center">
				<div class="header-container">
					<lottie-player
						src="https://lottie.host/94fc2f4b-5ad6-45a3-8ef7-cb3da2eb023c/QAI0JJymKZ.json"
						background="transparent"
						class="mx-auto"
						speed="1"
						style="width: 8rem; height: 8rem;"
						autoplay />
				</div>

				<h3 class="mb-0">
					QR Generator
				</h3>
				<p class="mb-4">
					<small>
						Generate your own QR code with customized design!
					</small>
				</p>

				<div class="mb-3">
					<form
						class="needs-validation"
						@submit.prevent>
						<div class="mb-3">
							<label class="form-label">Enter URL</label>
							
							<TheInput
								v-model="qrForm.url"
								type="type"
								placeholder="Enter link to open when scanned"
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
					</form>

					<button
						class="btn btn-primary text-center mb-3"
						:disabled="isLoading || v$.$invalid"
						@click="generateQR()">
						<span v-if="!isLoading">
							Generate
						</span>
						<span v-else>
							<i class="fa-solid fa-spinner fa-spin"></i>
						</span>
					</button>
					
					<div class="d-grid gap-2 d-flex justify-content-center">
						<button
							class="btn btn-outline-primary"
							:disabled="isLoading"
							@click="toggleModal()">
							Design
						</button>
	
						<button
							v-if="generatedResult !== null"
							class="btn btn-outline-primary"
							:disabled="generatedResult === null"
							@click="reset()">
							<span>
								Reset
							</span>
						</button>
					</div>
				</div>
			</div>

			<Transition>
				<div
					v-if="generatedResult"
					class="col-sm-12 col-md-3 text-center header-container">
					<div class="card bg-transparent">
						<div class="card-body shadow">
							<img
								v-if="generatedResult" 
								:src="`data:image/png;base64,${ generatedResult }`"
								class="rounded w-100 mb-3" />
							<div class="d-grid gap-2 d-flex justify-content-center">
								<button
									class="btn btn-outline-primary"
									@click="download()">
									<i class="fa-solid fa-download"></i>
									Download
								</button>
							</div>
						</div>
					</div>
				</div>
			</Transition>
		</div>

		<ModalComponent ref="modalComponent">
			<template #header>
				<span>
					Customize design
				</span>
			</template>

			<template #content>
				<form class="needs-validation">
					<div>
						<label class="form-label">Image type</label>
						<select
							v-model="qrForm.imageType"
							class="form-select">
							<option :value="ImageChoices.JPEG">
								JPEG
							</option>
							<option :value="ImageChoices.PNG">
								PNG
							</option>
						</select>
					</div>

					<hr class="my-3" />

					<label class="form-label">Style</label>
					<div class="row">
						<div class="col-sm-6 col-md-4">
							<img
								src="@/assets/images/qr/qr-example-1-square.png"
								role="button"
								class="rounded w-100 drawer-img"
								title="Square"
								:class="{
									'selected': qrForm.drawer === DrawerChoices.SQUAREM
								}"
								@click="onSelectDrawer(DrawerChoices.SQUAREM)" />
						</div>

						<div class="col-sm-6 col-md-4">
							<img
								src="@/assets/images/qr/qr-example-2-gapped.png"
								role="button"
								class="rounded w-100 drawer-img"
								title="Gapped square"
								:class="{
									'selected': qrForm.drawer === DrawerChoices.GAPPEDM
								}"
								@click="onSelectDrawer(DrawerChoices.GAPPEDM)" />
						</div>

						<div class="col-sm-6 col-md-4">
							<img
								src="@/assets/images/qr/qr-example-3-circle.png"
								role="button"
								class="rounded w-100 drawer-img"
								title="Circle"
								:class="{
									'selected': qrForm.drawer === DrawerChoices.CIRCLEM
								}"
								@click="onSelectDrawer(DrawerChoices.CIRCLEM)" />
						</div>

						<div class="col-sm-6 col-md-4">
							<img
								src="@/assets/images/qr/qr-example-4-rounded.png"
								role="button"
								class="rounded w-100 drawer-img"
								title="Rounded"
								:class="{
									'selected': qrForm.drawer === DrawerChoices.ROUNDEDM
								}"
								@click="onSelectDrawer(DrawerChoices.ROUNDEDM)" />
						</div>

						<div class="col-sm-6 col-md-4">
							<img
								src="@/assets/images/qr/qr-example-5-vertical.png"
								role="button"
								class="rounded w-100 drawer-img"
								title="Vertical"
								:class="{
									'selected': qrForm.drawer === DrawerChoices.VERTICALM
								}"
								@click="onSelectDrawer(DrawerChoices.VERTICALM)" />
						</div>

						<div class="col-sm-6 col-md-4">
							<img
								src="@/assets/images/qr/qr-example-6-horizontal.png"
								role="button"
								class="rounded w-100 drawer-img"
								title="Horizontal"
								:class="{
									'selected': qrForm.drawer === DrawerChoices.HORIZONTALM
								}"
								@click="onSelectDrawer(DrawerChoices.HORIZONTALM)" />
						</div>
					</div>

					<hr class="my-3" />

					<div class="row">
						<div class="col-6">
							<label class="form-label">Front color</label>
							<input
								v-model="qrForm.frontColor"
								type="color"
								class="form-control form-control-color p-0" />
						</div>

						<div class="col-6">
							<label class="form-label">Back color</label>
							<input
								v-model="qrForm.backColor"
								type="color"
								class="form-control form-control-color p-0" />
						</div>
					</div>
				</form>
			</template>

			<template #footer>
				<button
					type="button"
					class="btn btn-primary"
					@click="toggleModal()">
					Close
				</button>
			</template>
		</ModalComponent>
	</div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useServiceStore } from '@/store'

import { DrawerChoices, ImageChoices } from '@/helpers/qr-generator.enum'
import ModalComponent from '@/components/ModalComponent.vue'
import TheInput from '@/components/forms/TheInput.vue'

import useVuelidate from '@vuelidate/core'
import { helpers, required, url } from '@vuelidate/validators'

export default defineComponent({
	name: 'QRGeneratorView',
	components: {
		ModalComponent,
		TheInput
	},
	setup() {
		// Data
		const generatedResult = ref<string | null | unknown>(null)

		// Services
		const serviceSvc = useServiceStore()

		// Forms
		const qrForm = ref({
			url: null,
			imageType: ImageChoices.PNG,
			frontColor: '#000000',
			backColor: '#ffffff',
			drawer: DrawerChoices.SQUAREM
		})
		const validation = {
			url: { 
				required: helpers.withMessage(
					'Need to have a value',
					required
				),
				url: helpers.withMessage(
					'Need to have a valid url',
					url
				)
			}
		}
		const v$ = useVuelidate(validation, qrForm)

		// Checkers
		const isLoading = ref<boolean>(false)

		// Components
		const modalComponent = ref<InstanceType<typeof ModalComponent>>()

		// Generate QR
		const generateQR = () => {
			isLoading.value = true

			return serviceSvc.generateQR(
				qrForm.value
			).then(data => {
				generatedResult.value = data.result
				isLoading.value = false
			}).catch(() => {
				isLoading.value = false
			})
		}

		// Reset service
		const reset = () => {
			v$.value.$reset()
			qrForm.value.url = null
			generatedResult.value = null
		}

		// Download output
		const download = () => {
			const filetype_ = qrForm.value.imageType
			const source = `data:image/${ filetype_ };base64,${ generatedResult.value }`
			const fileName = 'qrcode_'
			const downloadLink = document.createElement('a')
			downloadLink.href = source
			downloadLink.download = `${ fileName }.${ filetype_ }`
			downloadLink.click()
		}

		// Toggle modal
		const toggleModal = () => {
			modalComponent.value?.toggleModal()
		}

		// Select drawer
		const onSelectDrawer = (mode: DrawerChoices) => {
			qrForm.value.drawer = mode
		}

		return {
			generatedResult,
			qrForm,
			v$,
			isLoading,
			modalComponent,
			generateQR,
			reset,
			download,
			toggleModal,
			onSelectDrawer,
			ImageChoices,
			DrawerChoices
		}
	}
})
</script>

<style lang="scss" scoped>
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
    transform: translateX(10px);
    opacity: 0;
}
.v-leave-to {
    transform: translateX(10px);
    opacity: 0;
}

.header-container {
	padding-top: 4rem;
	padding-bottom: 4rem;
}
</style>
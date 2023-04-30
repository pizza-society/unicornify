<template>
	<div class="container">
		<div class="d-flex flex-row vh-min justify-content-center row">
			<div class="col-lg-12 col-md-4 text-center">
				<div class="header-container">
					<lottie-player
						src="https://assets6.lottiefiles.com/packages/lf20_cdxs2q1x.json"
						background="transparent"
						class="mx-auto"
						speed="0.005"
						style="width: 8rem; height: 8rem;"
						loop
						autoplay />
				</div>

				<h3 class="mb-0">
					24 Hour Time Converter
				</h3>

				<p class="mb-4 text-secondary">
					<small>
						Convert 24 Hour to 12 Hour
					</small>
				</p>

				<div
					v-if="time"
					class="alert alert-primary alert-dismissible fade show"
					role="alert">
					<strong>
						Converted Time:
					</strong> 
					
					{{ time }}.
					<button
						type="button"
						class="btn-close"
						data-bs-dismiss="alert"
						aria-label="Close"
						@click="convertedTime = ''">
					</button>
				</div>

				<div class="mb-3">
					<form @submit.prevent>
						<div class="row rounded-top ">
							<div class="col mb-3">
								<label 
									for="input24H" 
									class="form-label">
									24 Hour Clock
								</label>

								<TheInput
									v-model="input24H"
									name="input24H"
									type="text"
									class="form-control mb-3"
									placeholder="00:00" />

								<button
									:disabled="input24H === '' ? true : false"
									class="btn btn-outline-primary"
									type="submit"
									@click="convertTime24to12">
									Convert to 12-hour
								</button>
							</div>

							<div class="col">
								<label
									for="input12H"
									class="form-label">12 Hour Clock
								</label>

								<TheInput
									v-model="input12H"
									name="input12H"
									type="text"
									class="form-control mb-3"
									placeholder="12:00 AM" />

								<button
									:disabled="input12H === '' ? true : false"
									class="btn btn-outline-primary"
									type="submit"
									@click="convertTime12to24">
									Convert to 24-hour
								</button>
							</div>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from 'vue'

import TheInput from '@/components/forms/TheInput.vue'
import { useToastStore } from '@/store/modules/toast.module'

const INVALID_24H = 'Invalid 24 Hour time format, valid format example: 18:00'
const INVALID_12H = 'Invalid 12 Hour time format, valid format example: 12:00 am'
const T24H_REGEX = /^(?:[01][0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?$/
const T12H_REGEX = /^(0?[1-9]|1[012])(:[0-5]\d) [APap][mM]$/
const AMPM_REGEX = /([0-9]{1,2}):([0-9]{2}) (AM|PM)/
const VALID_TIME_REGEX = /([0-9]{1,2}):([0-9]{2})/

export default defineComponent({
	name: 'ClockConverterView',
	components: { TheInput },
	setup() {
		// Data
		const input12H = ref<string>('')
		const input24H = ref<string>('')
		const convertedTime = ref<string>('')

		// Services
		const toastr = useToastStore()

		const convertTime24to12 = () => {
			const time24h = input24H.value.toUpperCase()
			// 24 hour regex
			const isValid = T24H_REGEX.test(time24h)
			const match = time24h.match(VALID_TIME_REGEX)

			if ((isValid || time24h === '24:00') && match) {
				const [sHours, minutes] = match.slice(1)
				const period = +sHours < 12 ? 'AM' : 'PM'
				const hours = +sHours % 12 || 12
				const output = `${ hours }:${ minutes } ${ period }`
				convertedTime.value = time24h === '24:00' ? '12:00 AM' : output
			} else {
				convertedTime.value = ''
				toastr.error(INVALID_24H)
			}
		}

		const convertTime12to24 = () => {
			const time12h = input12H.value.toUpperCase()
			// 12 hour regex
			const isValid = T12H_REGEX.test(time12h)
			const match = time12h.match(AMPM_REGEX)

			if (isValid && match) {
				const [sHours, minutes, period] = match.slice(1)
				const PM = period === 'PM'
				const hours = (+sHours % 12) + (PM ? 12 : 0)
				const output = `${ ('0' + hours).slice(-2) }:${ minutes }`
				convertedTime.value = output
			} else {
				convertedTime.value = ''
				toastr.error(INVALID_12H)
			}
		}

		const time = computed(() => {
			return convertedTime.value
		})
		
		return {
			convertedTime,
			input24H,
			convertTime24to12,
			input12H,
			convertTime12to24,
			time
		}
	}
})
</script>

<style lang="scss" scoped>
.header-container {
	padding-top: 4rem;
	padding-bottom: 4rem;
}

.container {
	max-width: 50rem;
}

div {
	text-align: center;
}

label {
	font-weight: bold;
}

input {
	text-align: center;
	min-width: 22rem;
}
</style>

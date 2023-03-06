<template>
	<div class="container">
		<div
			class="d-flex flex-column vh-min justify-content-center align-items-center">
			<!-- <lottie-player
				src="https://assets6.lottiefiles.com/packages/lf20_cdxs2q1x.json"
				background="transparent"
				speed="0.005"
				style="width: 300px; height: 300px;"
				loop
				autoplay/> -->

			<div class="col-lg-12 col-md-4 text-center">
				<h3 class="mb-0">
					24 Hour Time Converter
				</h3>

				<p class="mb-4">
					<small>
						Convert 24 Hour to 12 Hour
					</small>
				</p>

				<ErrorAlert v-if="error">
					{{ err }}
				</ErrorAlert>

				<div
					v-if="time"
					class="alert alert-primary alert-dismissible fade show"
					role="alert">
					<strong>
						Converted Time:
					</strong> 
					
					{{ time }}.
					<button
						@click="convertedTime = ''"
						type="button"
						class="btn-close"
						data-bs-dismiss="alert"
						aria-label="Close" />
				</div>

				<div class="mb-3">
					<form v-on:submit.prevent>

						<div class="row rounded-top ">
							<div class="col mb-3">
								<label 
									for="t24HourInput" 
									class="form-label">
									24 Hour Clock
								</label>

								<input
									name="t24HourInput"
									type="text"
									class="form-control mb-3"
									placeholder="00:00"
									v-model="t24HourInput"/>

								<button
									class="btn btn-outline-primary"
									type="submit"
									@click="convertTime24to12"
									:disabled="t24HourInput === '' ? true : false">
									Convert to 12-hour
								</button>

							</div>

							<div class="col">
								<label for="t12HourInput" class="form-label"
									>12 Hour Clock
								</label>

								<input
									name="t12HourInput"
									type="text"
									class="form-control mb-3"
									placeholder="12:00 AM"
									v-model="t12HourInput"/>

								<button
									class="btn btn-outline-primary"
									type="submit"
									@click="convertTime12to24"
									:disabled="t12HourInput === '' ? true : false">
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
import { defineComponent, ref, computed } from 'vue';

import ErrorAlert from '@/components/ErrorHandlers/ErrorAlert.vue';

export default defineComponent({
	name: 'ClockConverter',
	setup() {

		// Data
		const t12HourInput = ref<string>('')
		const t24HourInput = ref<string>('')
		const convertedTime = ref<string>('')
		const error = ref<boolean>(false)
		const errorMessage = ref<string>('')


		const convertTime24to12 = () => {
			const time24h = t24HourInput.value.toUpperCase()
			// 24 hour regex
			const isValid = /^(?:[01][0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?$/.test(time24h)
			const match = time24h.match(/([0-9]{1,2}):([0-9]{2})/)

			if ((isValid || time24h === '24:00') && match) {
				const [sHours, minutes] = match.slice(1)
				const period = +sHours < 12 ? 'AM' : 'PM'
				const hours = +sHours % 12 || 12
				const output = `${hours}:${minutes} ${period}`
				convertedTime.value = time24h === '24:00' ? '12:00 AM' : output
			} else {
				convertedTime.value = ''
				displayErrorMessage('Invalid 24 Hour time format, valid format example: 18:00', 3000)
			}
		}

		const convertTime12to24 = () => {
			const time12h = t12HourInput.value.toUpperCase()
			// 12 hour regex
			const isValid = /^(0?[1-9]|1[012])(:[0-5]\d) [APap][mM]$/.test(time12h)
			const match = time12h.match(/([0-9]{1,2}):([0-9]{2}) (AM|PM)/)

			if (isValid && match) {
				const [sHours, minutes, period] = match.slice(1)
				const PM = period === 'PM'
				const hours = (+sHours % 12) + (PM ? 12 : 0)
				const output = `${('0' + hours).slice(-2)}:${minutes}`
				convertedTime.value = output
			} else {
				convertedTime.value = ''
				displayErrorMessage('Invalid 12 Hour time format, valid format example: 12:00 am', 3000)
			}
		}

		const sleep = (time: number) => {
			return new Promise(resolve => setTimeout(resolve, time))
		}

		// Error Handler
		const displayErrorMessage = (context: string, duration: number) => {
			error.value = true
			errorMessage.value = context
			sleep(duration).then(() => {
				error.value = false
			})
		}

		const err = computed(() => {
			return errorMessage.value
		})

		const time = computed(() => {
			return convertedTime.value
		})
		return {
			convertedTime,
			t24HourInput,
			convertTime24to12,
			t12HourInput,
			convertTime12to24,
			err,
			error,
			time
		}
	},
	components: { ErrorAlert }
})
</script>

<style lang="scss" scoped>
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

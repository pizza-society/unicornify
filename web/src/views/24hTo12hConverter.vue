<template>
	<div class="container">
		<div
			class="d-flex flex-column justify-content-center align-items-center"
		>
			<lottie-player
				src="https://assets6.lottiefiles.com/packages/lf20_cdxs2q1x.json"
				background="transparent"
				speed="0.005"
				style="width: 300px; height: 300px;"
				loop
				autoplay
			/>
			<div class="col-lg-12 col-md-4 text-center">
				<h3 class="mb-0">
					Simple 24 Hour Time Converter
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
					role="alert"
				>
					<strong>Converted Time:</strong> {{ time }}.
					<button
						@click="convertedTime = null"
						type="button"
						class="btn-close"
						data-bs-dismiss="alert"
						aria-label="Close"
					/>
				</div>
				<div class="mb-3">
					<form v-on:submit.prevent>
						<div class="row rounded-top ">
							<div class="col mb-3">
								<label for="t24HourInput" class="form-label"
									>24 Hour Clock</label
								>
								<input
									name="t24HourInput"
									type="text"
									class="form-control mb-3"
									placeholder="00:00"
									v-model="t24HourInput"
								/>
								<button
									class="btn btn-outline-primary"
									type="submit"
									@click="convertTime24to12"
									:disabled="
										t24HourInput === '' ? true : false
									"
								>
									Convert to 12-hour
								</button>
							</div>
							<div class="col">
								<label for="t12HourInput" class="form-label"
									>12 Hour Clock</label
								>
								<input
									name="t12HourInput"
									type="text"
									class="form-control mb-3"
									placeholder="12:00 AM"
									v-model="t12HourInput"
								/>
								<button
									class="btn btn-outline-primary"
									type="submit"
									@click="convertTime12to24"
									:disabled="
										t12HourInput === '' ? true : false
									"
								>
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
import { defineComponent } from "vue";
import ErrorAlert from "@/components/ErrorHandlers/ErrorAlert.vue";
undefined;
export default defineComponent({
	name: "24h-to-12h-converter",
	data() {
		return {
			t12HourInput: "" as any,
			t24HourInput: "" as any,
			convertedTime: "" as any,
			error: false as boolean,
			errorMessage: "" as string
		};
	},
	methods: {
		convertTime24to12() {
			const time24h = this.t24HourInput.toUpperCase();
			// 24 hour regex
			const isValid = /^(?:[01][0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?$/.test(
				time24h
			);
			// console.log(isValid, time24h)
			if (isValid || time24h === "24:00") {
				const [sHours, minutes] = time24h
					.match(/([0-9]{1,2}):([0-9]{2})/)
					.slice(1);
				const period = +sHours < 12 ? "AM" : "PM";
				const hours = +sHours % 12 || 12;
				const output = `${hours}:${minutes} ${period}`;
				this.convertedTime = time24h === "24:00" ? "12:00 AM" : output;
			} else {
				this.convertedTime = null;
				this.displayErrorMessage(
					"Invalid 24 Hour time format, valid format example: 18:00",
					3000
				);
			}
		},
		convertTime12to24() {
			const time12h = this.t12HourInput.toUpperCase();
			// 12 hour regex
			const isValid = /^(0?[1-9]|1[012])(:[0-5]\d) [APap][mM]$/.test(
				time12h
			);
			// console.log(isValid, time12h)
			if (isValid) {
				const [sHours, minutes, period] = time12h
					.match(/([0-9]{1,2}):([0-9]{2}) (AM|PM)/)
					.slice(1);
				const PM = period === "PM";
				const hours = (+sHours % 12) + (PM ? 12 : 0);
				const output = `${("0" + hours).slice(-2)}:${minutes}`;
				this.convertedTime = output;
			} else {
				this.convertedTime = null;
				this.displayErrorMessage(
					"Invalid 12 Hour time format, valid format example: 12:00 am",
					3000
				);
			}
		},
		sleep(time: number) {
			return new Promise(resolve => setTimeout(resolve, time));
		},
		displayErrorMessage(context: string, duration: number) {
			this.error = true;
			this.errorMessage = context;
			// "Invalid 24 Hour time format, valid format example: 18:00";
			this.sleep(duration).then(() => {
				this.error = false;
			});
		}
	},
	computed: {
		err(): string {
			return this.errorMessage;
		},
		time(): string {
			return this.convertedTime;
		}
	},
	components: { ErrorAlert }
});
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

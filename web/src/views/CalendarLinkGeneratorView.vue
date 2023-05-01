<template>
	<div class="container">
		<div class="d-flex flex-row vh-min justify-content-center row gx-5">
			<div class="col-lg-8 mt-5">
				<div class="text-center">
					<h3 class="mb-0">
						Calendar Link Generator 
					</h3>
					<p class="mb-4 text-secondary">
						<small>
							Generate links to add an event to popular calendar services. 
						</small>
					</p>
				</div>

				<div class="mt-0">
					<form @submit.prevent>
						<small class="text-left text-secondary mt-3"> 
							DETAILS 
						</small>

						<hr class="mt-1" />

						<div class="row row-cols-12 gx-2 gy-3">
							<div class="col-12">
								<label 
									class="form-label">
									Title
								</label>

								<TheInput 
									v-model="calendarForm.title" 
									placeholder="Add Title" />
							</div>

							<div class="col-12 col-md-4">
								<label class="form-label">
									Location
								</label>

								<TheInput 
									v-model="calendarForm.location" 
									placeholder="Add Location" />
							</div>

							<div class="col-8 col-md-6">
								<label class="form-label">
									Timezone
								</label>

								<select
									v-model="calendarForm.timeZone"
									class="form-select">
									<option 
										v-if="calendarForm.timeZone != ''" 
										disabled
										value>
										Select a Timezone
									</option>

									<option
										v-else
										:value="calendarForm.timeZone">
										{{ Intl.DateTimeFormat().resolvedOptions().timeZone }}
									</option>

									<option 
										v-for="(zone, time) in timeZones" 
										:key="zone" 
										:value="zone">
										{{ time }}
									</option>
								</select>
							</div>

							<div class="col-4 col-md-2">
								<br />

								<div class="mt-3 form-check">
									<input 
										v-model="calendarForm.isAllDayEvent" 
										class="form-check-input" 
										type="checkbox" 
										placeholder="All day event" />

									<label 
										class="form-check-label"
										for="form-check-input">
										All Day
									</label>
								</div>
							</div>
						</div>

						<div class="row mt-1 mb-3 gy-3">
							<div class="col-12 col-md-6 mx-auto unicorn-calendar">
								<label
									class="form-check-label mb-2"
									for="date-time-picker">
									From
								</label>

								<DatePicker 
									v-model="calendarForm.startTime"
									name="date-time-picker"
									is-dark
									expanded
									title-position="left"
									:max-date="new Date()"
									:mode="calendarForm.isAllDayEvent ? 'date' : 'dateTime'" />
							</div>
							<div class="col-12 col-8 col-md-6 mx-auto">
								<label
									class="form-check-label mb-2"
									for="date-time-picker">
									To
								</label>

								<br />

								<DatePicker 
									v-model="calendarForm.endTime" 
									name="date-time-picker"
									is-dark
									expanded
									title-position="left"
									:min-date="new Date()"
									:mode="calendarForm.isAllDayEvent ? 'date' : 'dateTime'" />
							</div>
						</div>

						<div class="col-12 col-md-12 mx-auto">
							<div class="mb-3">
								<label
									for="form-control"
									class="form-label mb-2">
									Description
								</label>
                                
								<textarea
									class="form-control"
									rows="3"
									placeholder="Add description"></textarea>
							</div>
						</div>
					</form>
				</div>

				<div class="mt-2 mb-5">
					<small class="text-left text-secondary mt-3"> RESULTS </small>

					<hr class="mt-1" />

					<div class="row row-cols-1 gx-2 gy-3">
						<div class="col-12 mx-auto text-start">
							<span class="text-white fs-6 fs-md-8 mb-2">
								Google Calendar
							</span>
							<div class="input-group mt-1">
								<span class="input-group-text bg-body-tertiary">
									<!-- Google Calendar icon -->
									<i class="fa-brands fa-google"></i>
								</span>

								<input 
									type="text" 
									class="form-control" 
									placeholder="Google Calendar"
									readonly
									:value="generateGoogleCalendarLink" />

								<button
									class="btn btn-outline-secondary"
									@click="copyTextToClipboard(generateGoogleCalendarLink)">
									<i class="fa-sharp fa-solid fa-note-sticky"></i>
								</button>

								<a
									class="btn btn-outline-secondary"
									:href="generateGoogleCalendarLink">
									<i class="fa-sharp fa-solid fa-arrow-up-right-from-square"></i>
								</a>
							</div>
						</div>

						<div class="col-12 mx-auto text-start">
							<span class="text-white fs-6 fs-md-8 mb-2">
								Yahoo Calendar
							</span>
							<div class="input-group mt-1">
								<span class="input-group-text">
									<!-- Yahoo icon -->
									<i class="fa-brands fa-yahoo"></i>
								</span>
                                
								<input 
									type="text" 
									class="form-control" 
									placeholder="Yahoo Calendar"
									readonly
									:value="generateYahooCalendarLink" />

								<button
									class="btn btn-outline-secondary"
									@click="copyTextToClipboard(generateYahooCalendarLink)">
									<i class="fa-sharp fa-solid fa-note-sticky"></i>
								</button>

								<a
									class="btn btn-outline-secondary"
									:href="generateYahooCalendarLink">
									<i class="fa-sharp fa-solid fa-arrow-up-right-from-square"></i>
								</a>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts">
import {  computed, defineComponent, ref } from 'vue'

import { DatePicker } from 'v-calendar'

import { copyTextToClipboard } from '@/common/helpers'
import { TIME_ZONES } from '@/common/timezones'
import TheInput from '@/components/forms/TheInput.vue'


export default defineComponent({
	name: 'CalendarLinkGeneratorView',
	components: {
		DatePicker,
		TheInput
	},
	setup() {
		// Forms
		const calendarForm = ref({
			title: 'Event',
			location: '',
			startTime: new Date(),
			endTime: new Date(),
			timeZone: '',
			isAllDayEvent: false,
			fromDateHour: '',
			toDateHour: '',
			description: ''
		})

		/**
         * Converts a given date/datetime string or a Date object to a pure ISO 8601 string.
         * Returns a string in the format of YYYYMMDD or YYYYMMDDTHHmmSSZ depending on the value of isAllDayEvent.
         * @param {string | Date} dateTimeString - The date/datetime string or Date object to be converted.
         * @return {string} The converted ISO 8601 string.
         */
		const convertDateTimeToPureISO = (dateTimeString: string | Date) => {
			const date = new Date(new Date(dateTimeString))
			return calendarForm.value.isAllDayEvent
				? new Date(date.setDate(date.getDate() + 1))
					.toISOString()
					.split('T', 1)[0]
					.replace(/-/g, '')
				: date
					.toISOString()
					.replace(/-|:/g, '')
					.replace(/\.\d{3}Z/, 'Z')
		}

		// Computes
		const generateGoogleCalendarLink = computed(() => {
			return `https://calendar.google.com/calendar/render?action=TEMPLATE&text=${
				calendarForm.value.title
			}&details=${ calendarForm.value.description }&location=${
				calendarForm.value.location
			}&dates=${ convertDateTimeToPureISO(
				calendarForm.value.startTime
			) }%2F${ convertDateTimeToPureISO(calendarForm.value.endTime) }&ctz=${
				calendarForm.value.timeZone
			}`
		})

		const generateYahooCalendarLink = computed(() => {
			return `https://calendar.yahoo.com/?title=${
				calendarForm.value.title
			}&desc=${ calendarForm.value.description }&in_loc=${
				calendarForm.value.location
			}&st=${ convertDateTimeToPureISO(
				calendarForm.value.startTime
			) }&et=${ convertDateTimeToPureISO(calendarForm.value.endTime) }`
		})

		// Data
		const timeZones = TIME_ZONES
        
		return {
			calendarForm,
			generateGoogleCalendarLink,
			generateYahooCalendarLink,
			timeZones,
			copyTextToClipboard
		}
	}
})
</script>

<style lang="scss" scoped>
:deep(.vc-dark) {
	--vc-color: #adb5bd !important;
	--vc-bg: #212529 !important;
	--vc-border: #495057 !important;
	--vc-focus-ring: 0 0 0 2px rgb(139, 92, 246, 0.7);
	--vc-header-arrow-hover-bg: #171a1d !important;
	--vc-weekday-color: rgb(139, 92, 246, 0.8) !important;
	--vc-nav-title-color: #adb5bd !important;
	--vc-popover-content-bg: #212529 !important;
	--vc-popover-content-border: #495057 !important;
	--vc-time-picker-border: #495057 !important;
	--vc-time-weekday-color: #adb5bd !important;
	--vc-time-month-color: #8B5CF6 !important;
	--vc-time-day-color: #8B5CF6 !important;
	--vc-time-year-color: #adb5bd !important;
	--vc-time-select-group-bg: hsla(216, 15%, 52%, 0.3);
	--vc-time-select-group-border: transparent !important;
	--vc-highlight-solid-bg: #8B5CF6 !important;
	.vc-base-select select {
		border: 0 !important;
	}

	.vc-time-select-group .vc-base-icon {
		color: #8B5CF6;
	}

	.vc-day-content.vc-blue {
		background-color: #8B5CF6;
	}

	.vc-title, .vc-arrow, .vc-nav-title, .vc-nav-arrow,
	.vc-nav-item {
		background-color: #1a1e21;
	}

	.vc-nav-item {
		color: #adb5bd;

		&.is-active {
			background-color: #8B5CF6;
			color: #fff;
		}
	}
}
</style>
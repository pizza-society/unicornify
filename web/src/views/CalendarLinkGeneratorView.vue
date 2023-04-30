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

							<div class="col-4">
								<label class="form-label">
									Location
								</label>

								<TheInput 
									v-model="calendarForm.location" 
									placeholder="Add Location" />
							</div>

							<div class="col-6">
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

							<div class="col-2">
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

						<div class="row my-3">
							<div class="col-12 col-md-6 mx-auto">
								<label
									class="form-check-label mb-2"
									for="date-time-picker">
									From
								</label>

								<DatePicker 
									v-model="calendarForm.startTime"
									name="date-time-picker"
									color="purple"
									is-dark
									is-expanded
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
									color="purple"
									is-dark
									is-expanded
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
.header-container {
	padding-top: 4rem;
	padding-bottom: 4rem;
}
</style>
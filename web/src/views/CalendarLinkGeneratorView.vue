<template>
    <div class="container">
        <div class="d-flex flex-row vh-min justify-content-center row gx-5">
            <div class="col-lg-8 mt-5">
                <div class="text-center">
                    <h1 class="display-5 mb-0"> 
                        Calendar Link Generator 
                    </h1>

                    <p class="lead text-secondary"> 
                        Generate links to add an event to popular calendar services. 
                    </p>
                </div>

                <div class="mt-0">
                    <form @submit.prevent>
                        <small class="text-left text-secondary mt-3"> 
                            DETAILS 
                        </small>

                        <hr class="mt-1" />

                        <div class="row row-cols-2 g-4 gy-4">
                            <div class="col-7">
                                <label 
                                    class="form-label mb-1">
                                    Title
                                </label>

                                <input 
                                    class="form-control" 
                                    placeholder="Add Title" 
                                    v-model='calendarForm.title' />
                            </div>

                            <div class="col-4">
                                <label class="form-label mb-1">
                                    Location
                                </label>

                                <input 
                                    class="form-control" 
                                    placeholder="Add Location" 
                                    v-model='calendarForm.location' />
                            </div>

                            <div class="col-7">
                                <label class="form-label mb-1">
                                    Timezone
                                </label>

                                <select
                                    class="form-select"
                                    v-model='calendarForm.timeZone'>
                                    <option 
                                        v-if="calendarForm.timeZone != ''" 
                                        disabled value>
                                        Select a Timezone
                                    </option>

                                    <option v-else :value='calendarForm.timeZone'>
                                        {{ Intl.DateTimeFormat().resolvedOptions().timeZone }}
                                    </option>

                                    <option 
                                        v-for='(zone, time) in timeZones' 
                                        :value='zone' 
                                        :key='zone'>
                                        {{ time }}
                                    </option>
                                </select>
                            </div>

                            <div class="col-4">
                                <br />

                                <div class="mt-3 form-check">
                                    <input 
                                        class="form-check-input" 
                                        type="checkbox" 
                                        placeholder="All day event" 
                                        v-model='calendarForm.isAllDayEvent' />

                                    <label 
                                        class="form-check-label"
                                        for="form-check-inpu">
                                        All Day
                                    </label>
                                </div>
                            </div>
                        </div>

                        <div class="mt-2 mb-2">
                            <div class="col-11 mb-2">
                                <label
                                    class="form-check-label"
                                    for="date-time-picker">
                                    From
                                </label>

                                <br />

                                <DatePicker 
                                    name="date-time-picker"
                                    color="purple"
                                    is-dark
                                    is-expanded
                                    v-model="calendarForm.startTime"
                                    :max-date="new Date()"
                                    :mode="calendarForm.isAllDayEvent ? 'date' : 'dateTime'" />
                            </div>
                            <div class="col-11">
                                <label
                                    class="form-check-label"
                                    for="date-time-picker">
                                    To
                                </label>

                                <br />

                                <DatePicker 
                                    name="date-time-picker" 
                                    color="purple" 
                                    is-dark
                                    is-expanded
                                    v-model="calendarForm.endTime"
                                    :min-date="new Date()"
                                    :mode="calendarForm.isAllDayEvent ? 'date' : 'dateTime'" />
                            </div>
                        </div>

                        <div class="col-11">
                            <div class="mb-3">
                                <label for="form-control" class="form-label">
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

                    <div class="row row-cols-1 g-4 gy-4">
                        <div class="col-11">
                            <div class="input-group mb-3">
                                <span class="input-group-text">
                                    <!-- Google Calendar icon -->
                                    <i class="fa-brands fa-google"></i>
                                </span>

                                <input 
                                    type="text" 
                                    class="form-control" 
                                    placeholder="Google Calendar"
                                    readonly
                                    :value='generateGoogleCalendarLink'  />

                                <a 
                                    class="input-group-text" 
                                    @click='copyTextToClipboard(generateGoogleCalendarLink)'>
                                    <button
                                        type="button"
                                        class="btn btn-outline-dark">
                                        <i class="fa-sharp fa-solid fa-note-sticky"></i>
                                    </button>
                                </a>

                                <a
                                    id="basic-addon2"
                                    class="input-group-text"
                                    :href='generateGoogleCalendarLink'>
                                    <button
                                        type="button"
                                        class="btn btn-outline-dark">
                                        <i class="fa-sharp fa-solid fa-arrow-up-right-from-square"></i>
                                    </button>
                                </a>
                            </div>

                        </div>
                        <div class="col-11">
                            <div class="input-group mb-3">
                                <span class="input-group-text">
                                    <!-- Yahoo icon -->
                                    <i class="fa-brands fa-yahoo"></i>
                                </span>
                                
                                <input 
                                    type="text" 
                                    class="form-control" 
                                    placeholder="Yahoo Calendar"
                                    readonly
                                    :value='generateYahooCalendarLink' />

                                <span
                                    id="basic-addon3" 
                                    class="input-group-text" 
                                    @click='copyTextToClipboard(generateYahooCalendarLink)'>
                                    <button type="button" class="btn btn-outline-dark">
                                        <i class="fa-sharp fa-solid fa-note-sticky"></i>
                                    </button>
                                </span>

                                <a
                                    id="basic-addon4"
                                    class="input-group-text"
                                    :href='generateYahooCalendarLink'>
                                    <button
                                        type="button"
                                        class="btn btn-outline-dark">
                                        <i class="fa-sharp fa-solid fa-arrow-up-right-from-square"></i>
                                    </button>
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
import { defineComponent, ref } from 'vue'

import { DatePicker } from 'v-calendar'
import { computed } from '@vue/reactivity'

import { TIME_ZONES } from '@/common/timezones'
import { copyTextToClipboard } from '@/common/helpers'

export default defineComponent({
    name: 'CalendarLinkGenerator',
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
            }&details=${calendarForm.value.description}&location=${
                calendarForm.value.location
            }&dates=${convertDateTimeToPureISO(
                calendarForm.value.startTime
            )}%2F${convertDateTimeToPureISO(calendarForm.value.endTime)}&ctz=${
                calendarForm.value.timeZone
            }`
        })

        const generateYahooCalendarLink = computed(() => {
            return `https://calendar.yahoo.com/?title=${
                calendarForm.value.title
            }&desc=${calendarForm.value.description}&in_loc=${
                calendarForm.value.location
            }&st=${convertDateTimeToPureISO(
                calendarForm.value.startTime
            )}&et=${convertDateTimeToPureISO(calendarForm.value.endTime)}`
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
    },
    components: {
        DatePicker
    }
})
</script>

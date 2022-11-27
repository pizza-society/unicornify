<template>
    <div class="container">
        <div class="d-flex flex-row vh-min justify-content-center row gx-5">
            <div class="col-lg-8 mt-5">
                <div class="text-center">
                    <h1 class="display-5 mb-0"> Calendar Link Generator </h1>
                    <p class="lead text-secondary"> Generate links to add an event to popular calendar services. </p>
                </div>
                <div class="mt-0">
                    <form @submit.prevent>
                        <small class="text-left text-secondary mt-3"> DETAILS </small>
                        <hr class="mt-1" />
                        <div class="row row-cols-2 g-4 gy-4">
                            <div class="col-7">
                                <label class="form-label mb-1">Title</label>
                                <input class="form-control" placeholder="Add Title" v-model='calendarForm.title' />
                            </div>
                            <div class="col-4">
                                <label class="form-label mb-1">Location</label>
                                <input class="form-control" placeholder="Add Location" v-model='calendarForm.location' />
                            </div>
                            <div class="col-7">
                                <label class="form-label mb-1">Timezone</label>
                                <select class="form-select" v-model='calendarForm.timeZone'>
                                    <option v-if="calendarForm.timeZone != ''" disabled value>Select a Timezone</option>
                                    <option v-else :value='calendarForm.timeZone'>{{Intl.DateTimeFormat().resolvedOptions().timeZone}}</option>
                                    <option v-for='(zone, time) in timeZones' :value='zone' :key='zone'>
                                        {{time}}
                                    </option>
                                </select>
                            </div>
                            <div class="col-4">
                                <br />
                                <div class="mt-3 form-check">
                                    <input class="form-check-input" type="checkbox" placeholder="All day event" v-model='calendarForm.isAllDayEvent'>
                                    <label class="form-check-label" for="form-check-inpu">All Day</label>
                                </div>
                            </div>
                        </div>
                        <div class="mt-2 mb-2">
                            <div class="col-11 mb-2">
                                <label class="form-check-label" for="date-time-picker">From</label>
                                <br />
                                <DatePicker name="date-time-picker" :mode="calendarForm.isAllDayEvent ? 'date' : 'dateTime'" color="purple" is-dark is-expanded :max-date='new Date()' v-model='calendarForm.startTime' />
                            </div>
                            <div class="col-11">
                                <label class="form-check-label" for="date-time-picker">To</label>
                                <br />
                                <DatePicker name="date-time-picker" :mode="calendarForm.isAllDayEvent ? 'date' : 'dateTime'" color="purple" is-dark is-expanded :min-date='new Date()' v-model='calendarForm.endTime' />
                            </div>
                        </div>
                        <div class="col-11">
                            <div class="mb-3">
                                <label for="form-control" class="form-label">Description</label>
                                <textarea class="form-control" rows="3" placeholder="Add description"></textarea>
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
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="24" height="24">
                                        <rect width="22" height="22" x="13" y="13" fill="#fff"></rect>
                                        <polygon fill="#1e88e5" points="25.68,20.92 26.688,22.36 28.272,21.208 28.272,29.56 30,29.56 30,18.616 28.56,18.616"></polygon>
                                        <path fill="#1e88e5" d="M22.943,23.745c0.625-0.574,1.013-1.37,1.013-2.249c0-1.747-1.533-3.168-3.417-3.168 c-1.602,0-2.972,1.009-3.33,2.453l1.657,0.421c0.165-0.664,0.868-1.146,1.673-1.146c0.942,0,1.709,0.646,1.709,1.44 c0,0.794-0.767,1.44-1.709,1.44h-0.997v1.728h0.997c1.081,0,1.993,0.751,1.993,1.64c0,0.904-0.866,1.64-1.931,1.64 c-0.962,0-1.784-0.61-1.914-1.418L17,26.802c0.262,1.636,1.81,2.87,3.6,2.87c2.007,0,3.64-1.511,3.64-3.368 C24.24,25.281,23.736,24.363,22.943,23.745z"></path>
                                        <polygon fill="#fbc02d" points="34,42 14,42 13,38 14,34 34,34 35,38"></polygon>
                                        <polygon fill="#4caf50" points="38,35 42,34 42,14 38,13 34,14 34,34"></polygon>
                                        <path fill="#1e88e5" d="M34,14l1-4l-1-4H9C7.343,6,6,7.343,6,9v25l4,1l4-1V14H34z"></path>
                                        <polygon fill="#e53935" points="34,34 34,42 42,34"></polygon>
                                        <path fill="#1565c0" d="M39,6h-5v8h8V9C42,7.343,40.657,6,39,6z"></path>
                                        <path fill="#1565c0" d="M9,42h5v-8H6v5C6,40.657,7.343,42,9,42z"></path>
                                    </svg>
                                </span>
                                <input type="text" class="form-control" placeholder="Google Calendar" :value='generateGoogleCalendarLink' readonly>
                                <a class="input-group-text" id="basic-addon1" @click='copyURLToClipboard(generateGoogleCalendarLink)'>
                                    <button type="button" class="btn btn-outline-dark">
                                        <i class="fa-sharp fa-solid fa-note-sticky"></i>
                                    </button>
                                </a>
                                <a class="input-group-text" id="basic-addon2" :href='generateGoogleCalendarLink'>
                                    <button type="button" class="btn btn-outline-dark">
                                        <i class="fa-sharp fa-solid fa-arrow-up-right-from-square"></i>
                                    </button>
                                </a>
                            </div>
                        </div>
                        <div class="col-11">
                            <div class="input-group mb-3">
                                <span class="input-group-text">
                                    <!-- Yahoo icon -->
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="24" height="24">
                                        <path fill="#5c6bc0" d="M42,37c0,2.762-2.238,5-5,5H11c-2.761,0-5-2.238-5-5V11c0-2.762,2.239-5,5-5h26c2.762,0,5,2.238,5,5	V37z"></path>
                                        <path fill="#fff" d="M34,13H14c-0.552,0-1,0.448-1,1v12c0,0.552,0.448,1,1,1h20c0.552,0,1-0.448,1-1V14	C35,13.448,34.552,13,34,13z M33,17l-9,4l-9-4v-2h18V17z"></path>
                                        <g transform="matrix(.63072 0 0 .63072 -72.063 127.866)">
                                            <path fill="#fff" d="M132.266-150.491h2.385l1.389,3.552l1.407-3.552h2.322l-3.496,8.41h-2.337 l0.957-2.228L132.266-150.491z"></path>
                                            <path fill="#fff" d="M142.186-150.633c-1.792,0-2.924,1.607-2.924,3.207c0,1.801,1.242,3.228,2.89,3.228 c1.23,0,1.693-0.749,1.693-0.749v0.584h2.08v-6.128h-2.08v0.557C143.846-149.934,143.328-150.633,142.186-150.633z M142.629-148.663c0.827,0,1.253,0.654,1.253,1.244c0,0.636-0.457,1.259-1.253,1.259c-0.66,0-1.256-0.539-1.256-1.232 C141.372-148.095,141.852-148.663,142.629-148.663z"></path>
                                            <path fill="#fff" d="M146.642-144.363v-8.834h2.175v3.284c0,0,0.517-0.719,1.599-0.719 c1.324,0,2.099,0.986,2.099,2.396v3.873h-2.159v-3.343c0-0.477-0.227-0.938-0.742-0.938c-0.524,0-0.797,0.468-0.797,0.938v3.343 H146.642z"></path>
                                            <path fill="#fff" d="M156.224-150.632c-2.052,0-3.274,1.56-3.274,3.232c0,1.902,1.479,3.203,3.281,3.203 c1.747,0,3.275-1.241,3.275-3.171C159.507-149.479,157.907-150.632,156.224-150.632z M156.244-148.645 c0.725,0,1.226,0.604,1.226,1.247c0,0.549-0.467,1.226-1.226,1.226c-0.695,0-1.217-0.558-1.217-1.232 C155.027-148.053,155.46-148.645,156.244-148.645z"></path>
                                            <path fill="#fff" d="M163.131-150.632c-2.052,0-3.274,1.56-3.274,3.232c0,1.902,1.479,3.203,3.281,3.203 c1.747,0,3.275-1.241,3.275-3.171C166.414-149.479,164.814-150.632,163.131-150.632z M163.151-148.645 c0.725,0,1.226,0.604,1.226,1.247c0,0.549-0.467,1.226-1.226,1.226c-0.695,0-1.217-0.558-1.217-1.232 C161.933-148.053,162.367-148.645,163.151-148.645z"></path>
                                            <circle cx="168.131" cy="-145.677" r="1.445" fill="#fff"></circle>
                                            <path fill="#fff" d="M170.05-147.653h-2.601l2.308-5.545h2.591L170.05-147.653z"></path>
                                        </g>
                                    </svg>
                                </span>
                                <input type="text" class="form-control" placeholder="Yahoo Calendar" :value='generateYahooCalendarLink' readonly>
                                <span class="input-group-text" id="basic-addon3" @click='copyURLToClipboard(generateYahooCalendarLink)'>
                                    <button type="button" class="btn btn-outline-dark">
                                        <i class="fa-sharp fa-solid fa-note-sticky"></i>
                                    </button>
                                </span>
                                <a class="input-group-text" id="basic-addon4" :href='generateYahooCalendarLink'>
                                    <button type="button" class="btn btn-outline-dark">
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
import { defineComponent, ref } from 'vue';
import { DatePicker } from 'v-calendar';
import { computed } from '@vue/reactivity';
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
        });

        // Methods
        const copyURLToClipboard = async (text: string) => {
            await navigator.clipboard.writeText(text);
        };
        const convertDateTimeToPureISO = (dateTimeString: string | Date) => {
            /* 
                Return current ISO 8601 string without dash/hyphen
                if isAllDayEvent : -> return YYYYMMDD
                else : -> return YYYYMMDDTHHmmSSZ
            */
            const date = new Date(new Date(dateTimeString));
            return calendarForm.value.isAllDayEvent
                ? new Date(date.setDate(date.getDate() + 1))
                      .toISOString()
                      .split('T', 1)[0]
                      .replace(/-/g, '')
                : date
                      .toISOString()
                      .replace(/-|:/g, '')
                      .replace(/\.\d{3}Z/, 'Z');
        };

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
            }`;
        });

        const generateYahooCalendarLink = computed(() => {
            return `https://calendar.yahoo.com/?title=${
                calendarForm.value.title
            }&desc=${calendarForm.value.description}&in_loc=${
                calendarForm.value.location
            }&st=${convertDateTimeToPureISO(
                calendarForm.value.startTime
            )}&et=${convertDateTimeToPureISO(calendarForm.value.endTime)}`;
        });

        // Data
        const timeZones = {
            "Pacific/Midway": "Pacific/Midway (GMT-11:00)",
            "Pacific/Niue": "Pacific/Niue (GMT-11:00)",
            "Pacific/Pago_Pago": "Pacific/Pago Pago (GMT-11:00)",
            "America/Adak": "America/Adak (GMT-10:00)",
            "Pacific/Honolulu": "Pacific/Honolulu (GMT-10:00)",
            "Pacific/Rarotonga": "Pacific/Rarotonga (GMT-10:00)",
            "Pacific/Tahiti": "Pacific/Tahiti (GMT-10:00)",
            "Pacific/Marquesas": "Pacific/Marquesas (GMT-09:30)",
            "America/Anchorage": "America/Anchorage (GMT-09:00)",
            "America/Juneau": "America/Juneau (GMT-09:00)",
            "America/Metlakatla": "America/Metlakatla (GMT-09:00)",
            "America/Nome": "America/Nome (GMT-09:00)",
            "America/Sitka": "America/Sitka (GMT-09:00)",
            "America/Yakutat": "America/Yakutat (GMT-09:00)",
            "Pacific/Gambier": "Pacific/Gambier (GMT-09:00)",
            "America/Los_Angeles": "America/Los Angeles (GMT-08:00)",
            "America/Tijuana": "America/Tijuana (GMT-08:00)",
            "America/Vancouver": "America/Vancouver (GMT-08:00)",
            "Pacific/Pitcairn": "Pacific/Pitcairn (GMT-08:00)",
            "America/Boise": "America/Boise (GMT-07:00)",
            "America/Cambridge_Bay": "America/Cambridge Bay (GMT-07:00)",
            "America/Chihuahua": "America/Chihuahua (GMT-07:00)",
            "America/Creston": "America/Creston (GMT-07:00)",
            "America/Dawson": "America/Dawson (GMT-07:00)",
            "America/Dawson_Creek": "America/Dawson Creek (GMT-07:00)",
            "America/Denver": "America/Denver (GMT-07:00)",
            "America/Edmonton": "America/Edmonton (GMT-07:00)",
            "America/Fort_Nelson": "America/Fort Nelson (GMT-07:00)",
            "America/Hermosillo": "America/Hermosillo (GMT-07:00)",
            "America/Inuvik": "America/Inuvik (GMT-07:00)",
            "America/Mazatlan": "America/Mazatlan (GMT-07:00)",
            "America/Ojinaga": "America/Ojinaga (GMT-07:00)",
            "America/Porto_Velho": "America/Porto Velho (GMT-04:00)",
            "America/Port_of_Spain": "America/Port of Spain (GMT-04:00)",
            "America/Puerto_Rico": "America/Puerto Rico (GMT-04:00)",
            "America/Santiago": "America/Santiago (GMT-04:00)",
            "America/Santo_Domingo": "America/Santo Domingo (GMT-04:00)",
            "America/St_Barthelemy": "America/St Barthelemy (GMT-04:00)",
            "America/St_Kitts": "America/St Kitts (GMT-04:00)",
            "America/St_Lucia": "America/St Lucia (GMT-04:00)",
            "America/St_Thomas": "America/St Thomas (GMT-04:00)",
            "America/St_Vincent": "America/St Vincent (GMT-04:00)",
            "America/Thule": "America/Thule (GMT-04:00)",
            "America/Tortola": "America/Tortola (GMT-04:00)",
            "Atlantic/Bermuda": "Atlantic/Bermuda (GMT-04:00)",
            "America/St_Johns": "America/St Johns (GMT-03:30)",
            "America/Araguaina": "America/Araguaina (GMT-03:00)",
            "America/Argentina/Buenos_Aires": "America/Argentina/Buenos Aires (GMT-03:00)",
            "America/Argentina/Catamarca": "America/Argentina/Catamarca (GMT-03:00)",
            "America/Argentina/Cordoba": "America/Argentina/Cordoba (GMT-03:00)",
            "Africa/Ndjamena": "Africa/Ndjamena (GMT+01:00)",
            "Africa/Niamey": "Africa/Niamey (GMT+01:00)",
            "Africa/Porto-Novo": "Africa/Porto-Novo (GMT+01:00)",
            "Africa/Tunis": "Africa/Tunis (GMT+01:00)",
            "Africa/Windhoek": "Africa/Windhoek (GMT+01:00)",
            "Arctic/Longyearbyen": "Arctic/Longyearbyen (GMT+01:00)",
            "Europe/Amsterdam": "Europe/Amsterdam (GMT+01:00)",
            "Europe/Andorra": "Europe/Andorra (GMT+01:00)",
            "Europe/Belgrade": "Europe/Belgrade (GMT+01:00)",
            "Europe/Berlin": "Europe/Berlin (GMT+01:00)",
            "Europe/Bratislava": "Europe/Bratislava (GMT+01:00)",
            "Europe/Brussels": "Europe/Brussels (GMT+01:00)",
            "Europe/Budapest": "Europe/Budapest (GMT+01:00)",
            "Europe/Copenhagen": "Europe/Copenhagen (GMT+01:00)",
            "Europe/Gibraltar": "Europe/Gibraltar (GMT+01:00)",
            "Europe/Ljubljana": "Europe/Ljubljana (GMT+01:00)",
            "Europe/Luxembourg": "Europe/Luxembourg (GMT+01:00)",
            "Europe/Madrid": "Europe/Madrid (GMT+01:00)",
            "Europe/Malta": "Europe/Malta (GMT+01:00)",
            "Europe/Monaco": "Europe/Monaco (GMT+01:00)",
            "Europe/Oslo": "Europe/Oslo (GMT+01:00)",
            "Europe/Paris": "Europe/Paris (GMT+01:00)",
            "Europe/Podgorica": "Europe/Podgorica (GMT+01:00)",
            "Europe/Prague": "Europe/Prague (GMT+01:00)",
            "Europe/Rome": "Europe/Rome (GMT+01:00)",
            "Europe/San_Marino": "Europe/San Marino (GMT+01:00)",
            "Europe/Sarajevo": "Europe/Sarajevo (GMT+01:00)",
            "Europe/Skopje": "Europe/Skopje (GMT+01:00)",
            "Europe/Stockholm": "Europe/Stockholm (GMT+01:00)",
            "Europe/Tirane": "Europe/Tirane (GMT+01:00)",
            "Europe/Vaduz": "Europe/Vaduz (GMT+01:00)",
            "Europe/Vatican": "Europe/Vatican (GMT+01:00)",
            "Europe/Vienna": "Europe/Vienna (GMT+01:00)",
            "Europe/Warsaw": "Europe/Warsaw (GMT+01:00)",
            "Europe/Zagreb": "Europe/Zagreb (GMT+01:00)",
            "Europe/Zurich": "Europe/Zurich (GMT+01:00)",
            "Africa/Blantyre": "Africa/Blantyre (GMT+02:00)",
            "Africa/Bujumbura": "Africa/Bujumbura (GMT+02:00)",
            "Africa/Cairo": "Africa/Cairo (GMT+02:00)",
            "Africa/Gaborone": "Africa/Gaborone (GMT+02:00)",
            "Africa/Harare": "Africa/Harare (GMT+02:00)",
            "Africa/Johannesburg": "Africa/Johannesburg (GMT+02:00)",
            "Africa/Juba": "Africa/Juba (GMT+02:00)",
            "Africa/Khartoum": "Africa/Khartoum (GMT+02:00)",
            "Africa/Kigali": "Africa/Kigali (GMT+02:00)",
            "Africa/Lubumbashi": "Africa/Lubumbashi (GMT+02:00)",
            "Africa/Lusaka": "Africa/Lusaka (GMT+02:00)",
            "Africa/Maputo": "Africa/Maputo (GMT+02:00)",
            "Africa/Maseru": "Africa/Maseru (GMT+02:00)",
            "Africa/Mbabane": "Africa/Mbabane (GMT+02:00)",
            "Africa/Tripoli": "Africa/Tripoli (GMT+02:00)",
            "Asia/Amman": "Asia/Amman (GMT+02:00)",
            "Asia/Beirut": "Asia/Beirut (GMT+02:00)",
            "Asia/Damascus": "Asia/Damascus (GMT+02:00)",
            "Asia/Famagusta": "Asia/Famagusta (GMT+02:00)",
        }
        
        return {
            calendarForm,
            generateGoogleCalendarLink,
            generateYahooCalendarLink,
            timeZones,
            copyURLToClipboard
        };
    },
    components: {
        DatePicker
    }
});
</script>
<style lang="scss" scoped></style>

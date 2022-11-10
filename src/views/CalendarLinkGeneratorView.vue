<template>
    <div class="container">
        <div class="d-flex flex-row vh-min justify-content-center row gx-5">
            <div class="col-lg-8 mt-5 ">
                <div class="text-center">
                    <h1 class="display-5 mb-0">
                        Calendar Link Generator
                    </h1>
                    <p class="lead text-secondary ">
                        Generate links to add an event to popular calendar services.
                    </p>
                </div>
                <div>
                    <div class="mt-0">
                        <form @submit.prevent>
                            <small class="text-left text-secondary mt-3">
                            DETAILS
                            </small>
                            <hr class="mt-1"/>
                            <div class="row row-cols-2 g-4 gy-4">
                                <div class="col-7">
                                    <label class="form-label mb-1">Title</label>
                                    <input class="form-control" placeholder="Add Title" v-model="calendarForm.title"/>
                                </div>
                                <div class="col-4">
                                    <label class="form-label mb-1">Location</label>
                                    <input class="form-control" placeholder="Add Location" v-model="calendarForm.location"/>
                                </div>
                                <div class="col-7">
                                    <label class="form-label mb-1">Timezone</label>
                                    <select name="timezone_offset" id="timezone-offset" class="form-select" v-model="calendarForm.timeZone">
                                        <option value="-12:00">(GMT -12:00) Eniwetok, Kwajalein</option>
                                        <option value="-11:00">(GMT -11:00) Midway Island, Samoa</option>
                                        <option value="-10:00">(GMT -10:00) Hawaii</option>
                                        <option value="-09:50">(GMT -9:30) Taiohae</option>
                                        <option value="-09:00">(GMT -9:00) Alaska</option>
                                        <option value="-08:00">(GMT -8:00) Pacific Time (US &amp; Canada)</option>
                                        <option value="-07:00">(GMT -7:00) Mountain Time (US &amp; Canada)</option>
                                        <option value="-06:00">(GMT -6:00) Central Time (US &amp; Canada), Mexico City</option>
                                        <option value="-05:00">(GMT -5:00) Eastern Time (US &amp; Canada), Bogota, Lima</option>
                                        <option value="-04:50">(GMT -4:30) Caracas</option>
                                        <option value="-04:00">(GMT -4:00) Atlantic Time (Canada), Caracas, La Paz</option>
                                        <option value="-03:50">(GMT -3:30) Newfoundland</option>
                                        <option value="-03:00">(GMT -3:00) Brazil, Buenos Aires, Georgetown</option>
                                        <option value="-02:00">(GMT -2:00) Mid-Atlantic</option>
                                        <option value="-01:00">(GMT -1:00) Azores, Cape Verde Islands</option>
                                        <option value="+00:00">(GMT) Western Europe Time, London, Lisbon, Casablanca</option>
                                        <option value="+01:00">(GMT +1:00) Brussels, Copenhagen, Madrid, Paris</option>
                                        <option value="+02:00">(GMT +2:00) Kaliningrad, South Africa</option>
                                        <option value="+03:00">(GMT +3:00) Baghdad, Riyadh, Moscow, St. Petersburg</option>
                                        <option value="+03:50">(GMT +3:30) Tehran</option>
                                        <option value="+04:00">(GMT +4:00) Abu Dhabi, Muscat, Baku, Tbilisi</option>
                                        <option value="+04:50">(GMT +4:30) Kabul</option>
                                        <option value="+05:00">(GMT +5:00) Ekaterinburg, Islamabad, Karachi, Tashkent</option>
                                        <option value="+05:50">(GMT +5:30) Bombay, Calcutta, Madras, New Delhi</option>
                                        <option value="+05:75">(GMT +5:45) Kathmandu, Pokhara</option>
                                        <option value="+06:00">(GMT +6:00) Almaty, Dhaka, Colombo</option>
                                        <option value="+06:50">(GMT +6:30) Yangon, Mandalay</option>
                                        <option value="+07:00">(GMT +7:00) Bangkok, Hanoi, Jakarta</option>
                                        <option value="+08:00">(GMT +8:00) Beijing, Perth, Singapore, Hong Kong</option>
                                        <option value="+08:75">(GMT +8:45) Eucla</option>
                                        <option value="+09:00">(GMT +9:00) Tokyo, Seoul, Osaka, Sapporo, Yakutsk</option>
                                        <option value="+09:50">(GMT +9:30) Adelaide, Darwin</option>
                                        <option value="+10:00">(GMT +10:00) Eastern Australia, Guam, Vladivostok</option>
                                        <option value="+10:50">(GMT +10:30) Lord Howe Island</option>
                                        <option value="+11:00">(GMT +11:00) Magadan, Solomon Islands, New Caledonia</option>
                                        <option value="+11:50">(GMT +11:30) Norfolk Island</option>
                                        <option value="+12:00">(GMT +12:00) Auckland, Wellington, Fiji, Kamchatka</option>
                                        <option value="+12:75">(GMT +12:45) Chatham Islands</option>
                                        <option value="+13:00">(GMT +13:00) Apia, Nukualofa</option>
                                        <option value="+14:00">(GMT +14:00) Line Islands, Tokelau</option>
                                    </select>
                                </div>
                                <div class="col-4">
                                    <br/>
                                    <div class="mt-3 form-check">
                                        <input class="form-check-input" type="checkbox" placeholder="All day event" v-model="calendarForm.isAllDayEvent">
                                        <label class="form-check-label" for="form-check-inpu">All day event</label>
                                    </div>
                                </div>
                                <div class="col-6">
                                    <label class="form-check-label" for="date-time-picker">From</label>
                                    <br/>
                                    <DatePicker 
                                        name="date-time-picker"
                                        :mode = "calendarForm.isAllDayEvent ? 'date' : 'dateTime'" 
                                        color="purple"
                                        is-dark
                                        is-expanded
                                        :max-date='new Date()'
                                        v-model="calendarForm.startTime" 
                                        />
                                </div>
                                <div class="col-6">
                                    <label class="form-check-label" for="date-time-picker">To</label>
                                    <br/>
                                    <DatePicker 
                                        name="date-time-picker"
                                        :mode = "calendarForm.isAllDayEvent ? 'date' : 'dateTime'" 
                                        color="purple"
                                        is-dark
                                        is-expanded
                                        :min-date='new Date()'
                                        v-model="calendarForm.endTime" 
                                        />
                                </div>
                                <div class="col-11">
                                    <div class="mb-3">
                                        <label for="form-control" class="form-label">Description</label>
                                        <textarea class="form-control" rows="3" placeholder="Add description"></textarea>
                                    </div>
                                </div>
                            </div>
                        </form>
                    </div>
                    <div class="mt-2 mb-5">
                        <small class="text-left text-secondary mt-3">
                        RESULTS
                        </small>
                        <hr class="mt-1"/>
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
                                    <input type="text" class="form-control" placeholder="Google Calendar"  :value="generateGoogleCalendarLink" readonly>
                                </div>
                            </div>
                            <div class="col-11">
                                <div class="input-group mb-3">
                                    <span class="input-group-text">
                                        <!-- Outlook icon -->
                                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="24" height="24">
                                            <path fill="#03A9F4" d="M21,31c0,1.104,0.896,2,2,2h17c1.104,0,2-0.896,2-2V16c0-1.104-0.896-2-2-2H23c-1.104,0-2,0.896-2,2V31z"></path>
                                            <path fill="#B3E5FC" d="M42,16.975V16c0-0.428-0.137-0.823-0.367-1.148l-11.264,6.932l-7.542-4.656L22.125,19l8.459,5L42,16.975z"></path>
                                            <path fill="#0277BD" d="M27 41.46L6 37.46 6 9.46 27 5.46z"></path>
                                            <path fill="#FFF" d="M21.216,18.311c-1.098-1.275-2.546-1.913-4.328-1.913c-1.892,0-3.408,0.669-4.554,2.003c-1.144,1.337-1.719,3.088-1.719,5.246c0,2.045,0.564,3.714,1.69,4.986c1.126,1.273,2.592,1.91,4.378,1.91c1.84,0,3.331-0.652,4.474-1.975c1.143-1.313,1.712-3.043,1.712-5.199C22.869,21.281,22.318,19.595,21.216,18.311z M19.049,26.735c-0.568,0.769-1.339,1.152-2.313,1.152c-0.939,0-1.699-0.394-2.285-1.187c-0.581-0.785-0.87-1.861-0.87-3.211c0-1.336,0.289-2.414,0.87-3.225c0.586-0.81,1.368-1.211,2.355-1.211c0.962,0,1.718,0.393,2.267,1.178c0.555,0.795,0.833,1.895,0.833,3.31C19.907,24.906,19.618,25.968,19.049,26.735z"></path>
                                        </svg>
                                    </span>
                                    <input type="text" class="form-control" placeholder="Outlook Calendar" readonly>
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
                                    <input type="text" class="form-control" placeholder="Yahoo Calendar" readonly>
                                </div>
                            </div>
                            <div class="col-12 ">
                                <button type="button" class="btn btn-secondary text-primay rounded-2">DOWNLOAD ICS</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script lang="ts">
import { defineComponent, ref } from "vue";
import { DatePicker } from "v-calendar";
import { computed } from "@vue/reactivity";
export default defineComponent({
	name: "CalendarLinkGenerator",
	setup() {
		// Forms
		const calendarForm = ref({
			title: "",
			location: "",
			startTime: new Date(),
			endTime: new Date(),
			timeZone: new Date(),
			isAllDayEvent: false,
			fromDateHour: "",
			toDateHour: "",
			description: ""
		});

		// Methods
		const convertDateTimeToISO = (dateTimeString: string | Date) => {
			return new Date(new Date(dateTimeString)).toISOString();
		};

		console.log("calendarForm", calendarForm.value.title);
        // https://calendar.google.com/calendar/render?action=TEMPLATE&dates=20221110%2F20221111&details=&location=&text=
        // https://calendar.google.com/calendar/render?action=TEMPLATE&dates=20221110T151500Z%2F20221110T151500Z&details=&location=&text=
		const generateGoogleCalendarLink = computed(() => {
			return `https://www.google.com/calendar/render?action=TEMPLATE&text=${
				calendarForm.value.title
			}&details=${calendarForm.value.description}&location=${
				calendarForm.value.location
			}&dates=${convertDateTimeToISO(
				calendarForm.value.startTime
			)}/${convertDateTimeToISO(calendarForm.value.endTime)}`;
		});

		return { calendarForm, generateGoogleCalendarLink };
	},
	components: {
		DatePicker
	}
});
</script>
<style lang="scss" scoped></style>

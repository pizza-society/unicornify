<template>
  <div class="container">
      <div class="d-flex flex-row vh-min justify-content-center row gx-5">
          <!-- <h1 class="display-6">This Google Calendar LinkGenerator</h1> -->
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
                      <small class="text-left text-secondary mt-3">
                      DETAILS
                      </small>
                      <hr class="mt-1"/>
                      <div class="row row-cols-2 g-4 gy-4">
                          <div class="col-7">
                              <label class="form-label mb-1">Title</label>
                              <input class="form-control" placeholder="Add Title"/>
                          </div>
                          <div class="col-4">
                              <label class="form-label mb-1">Location</label>
                              <input class="form-control" placeholder="Add Location"/>
                          </div>
                          <div class="col-7">
                              <label class="form-label mb-1">Timezone</label>
                              <!-- https://gist.github.com/nodesocket/3919205 -->
                              <select name="timezone_offset" id="timezone-offset" class="form-select">
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
                                  <input class="form-check-input" type="checkbox" placeholder="All day event" value="">
                                  <label class="form-check-label" for="form-check-inpu">All day event</label>
                              </div>
                          </div>
                          <div class="col-7">
                              <label class="form-check-label" for="date-time-picker">From</label>
                              <br/>
                              <DatePicker 
                                  name="date-time-picker"
                                  mode="dateTime" 
                                  color="purple"
                                  is-dark
                                  is-expanded
                                  />
                          </div>
                          <div class="col-4">
                              <label class="form-check-label" for="date-time-picker">To</label>
                              <br/>
                              <DatePicker 
                                  name="date-time-picker"
                                  mode="dateTime" 
                                  color="purple"
                                  is-dark
                                  is-expanded
                                  />
                          </div>
                      </div>
                  </div>
              </div>
          </div>
      </div>
  </div>
</template>
<script lang="ts">
  import { defineComponent } from 'vue';
  import { DatePicker } from 'v-calendar';
  export default defineComponent({
    name: 'GoogleCalendarLinkGenerator',
    setup() {

      return {}
    },
    components: {
      DatePicker
    },
  });
</script>
<style lang="scss" scoped></style>
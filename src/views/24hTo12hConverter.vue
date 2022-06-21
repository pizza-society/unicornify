<template>
    <div class="container pt-5">
        <div
            class="d-flex flex-column justify-content-center align-items-center">
            <ErrorAlert v-if="error">
                An Error has occured, please try again later ...
            </ErrorAlert>
            <h1 class="display-6">
                <b>Time Converter - Convert 24 Hour to 12 Hour</b>
            </h1>
            <lottie-player
                src="https://assets6.lottiefiles.com/packages/lf20_cdxs2q1x.json"
                background="transparent"
                speed="0.10"
                style="width: 350px; height: 350px;"
                loop
                autoplay/>
            <div>
                <div class="container">
                    <div class="row rounded-top ">
                        <div class="col">
                            <label for="exampleInputEmail1" class="form-label"
                                >24 Hour Clock</label>
                            <input
                                type="email"
                                class="form-control"
                                placeholder="00:00"
                                v-model="t24HourInput"/>
                            <br />
                            <button
                                class="btn btn-outline-primary"
                                type="submit"
                                id="button-addon1"
                                @click="convertTime24to12">
                                Convert to 12-hour
                            </button>
                        </div>
                        <div class="col">
                            <label for="exampleInputEmail1" class="form-label">12 Hour Clock</label>
                            <input
                                type="email"
                                class="form-control"
                                placeholder="12:00 AM"
                                v-model="t12HourInput"
                            />
                            <br />
                            <button
                                class="btn btn-outline-primary"
                                type="submit"
                                id="button-addon1"
                                @click="convertTime12to24">
                                Convert to 24-hour
                            </button>
                        </div>
                    </div>
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
            error: false as boolean
        };
    },
    methods: {
        convertTime24to12() {
            const time24h = this.t24HourInput;
            const [sHours, minutes] = time24h
                .match(/([0-9]{1,2}):([0-9]{2})/)
                .slice(1);
            const period = +sHours < 12 ? "AM" : "PM";
            const hours = +sHours % 12 || 12;
            const output = `${hours}:${minutes} ${period}`;
            console.log(output);
            // return `${hours}:${minutes} ${period}`;
        },
        convertTime12to24() {
            const time12h = this.t12HourInput;
            const [sHours, minutes, period] = time12h
                .match(/([0-9]{1,2}):([0-9]{2}) (AM|PM)/)
                .slice(1);
            const PM = period === "PM";
            const hours = (+sHours % 12) + (PM ? 12 : 0);
            const output = `${("0" + hours).slice(-2)}:${minutes}`;
            console.log(output);
            // return `${('0' + hours).slice(-2)}:${minutes}`;
        },
        sleep(time: number) {
            return new Promise(resolve => setTimeout(resolve, time));
        }
    },
    computed: {},
    components: { ErrorAlert }
});
</script>

<style lang="scss" scoped>
.container-sm {
    max-width: 50rem;
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

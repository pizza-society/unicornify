<template>
	<div class="container">
		<div
			class="d-flex flex-row vh-min justify-content-center align-items-center row"
		>
			<div class="col-lg-12 col-md-4 text-center">
				<ErrorAlert v-if="error">
					An Error has occured, please try again later ...
				</ErrorAlert>
				<h3 class="mb-0">
					Disposable Email Validator
				</h3>
				<p class="mb-4">
					<small>
						Validate disposable email address in seconds !
					</small>
				</p>
				<div class="mb-3">
					<div v-if="!formSubmitted">
						<div class="container-sm">
							<form @submit="validateEmail()" v-on:submit.prevent>
								<div v-if="!formSubmitted">
									<label class="form-label"
										>Enter An Email</label
									>
									<input
										type="email"
										class="form-control"
										placeholder="Email address"
										aria-label="Email address"
										aria-describedby="button-addon1"
										v-model="userEmail.email"
										required
									/>
									<br />
									<button
										class="btn btn-outline-primary"
										type="submit"
										id="button-addon1"
									>
										Verify
									</button>
								</div>
							</form>
						</div>
					</div>
					<div
						v-else-if="
							dataObtained &&
								!response.disposable &&
								response.format
						"
					>
						<div class="alert alert-success" role="alert">
							The Email <b>"{{ email }}"</b> is Valid and Not
							Disposable
						</div>
					</div>
					<div v-else-if="dataObtained && response.disposable">
						<div class="alert alert-danger" role="alert">
							Warning, The Email <b>"{{ email }}"</b> is a
							Disposable Email.
						</div>
					</div>
					<div v-else-if="dataObtained && !response.format">
						<div class="alert alert-light" role="alert">
							The Email <b>"{{ email }}"</b> is not a Valid Email.
						</div>
					</div>
					<div v-else>
						<div class="spinner-border" role="status">
							<span class="visually-hidden">Loading...</span>
						</div>
					</div>
					<br />
					<button
						v-if="dataObtained"
						type="button"
						class="btn btn-primary btn-lg"
						@click="$router.go(0)"
					>
						Check again
					</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import ErrorAlert from "@/components/ErrorHandlers/ErrorAlert.vue";
import { useServiceStore } from "@/store";
import { mapActions } from "pinia";

undefined;
export default defineComponent({
	name: "email-validator",
	data() {
		return {
			userEmail: { email: "" } as any,
			formSubmitted: false as boolean,
			dataObtained: false as boolean,
			response: "" as any,
			error: false as boolean
		};
	},
	methods: {
		...mapActions(useServiceStore, ["validateDisposableEmail"]),
		validateEmail() {
			this.formSubmitted = true;
			this.validateDisposableEmail(this.userEmail)
				.then(response => {
					// console.log("Response", response.data);
					this.response = response.data;
					this.dataObtained = true;
					this.sleep(3000).then(() => {
						this.dataObtained = true;
					});
				})
				.catch(err => {
					console.log("Error", err);
					this.error = true;
					// setTimeout(() => this.$router.push({ name: "home" }), 5000);
				});
			// axios
			// 	.get(`https://www.disify.com/api/email/${this.userEmail}`)
			// 	.then((response: ResponseData) => {
			// 		// console.log("Response", response.data);
			// 		this.response = response.data;
			// 		this.dataObtained = true;
			// 		// this.sleep(3000).then(() => {
			// 		//     this.dataObtained = true;
			// 		// });
			// 	})
			// 	.catch(err => {
			// 		console.log("Error", err);
			// 		this.error = true;
			// 		setTimeout(() => this.$router.push({ name: "home" }), 5000);
			// 	});
		},
		sleep(time: number) {
			return new Promise(resolve => setTimeout(resolve, time));
		}
	},
	computed: {
		email(): string {
			return this.userEmail.email + "!";
		}
	},
	components: { ErrorAlert }
});
</script>
<style lang="scss" scoped>
.container-sm {
	max-width: 25rem;
}

.container {
	max-width: 50rem;
}
</style>

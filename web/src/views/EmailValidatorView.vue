<template>
	<div class="container">
		<div class="d-flex flex-row vh-min justify-content-center row">
			<div class="col-sm-12 col-md-4 text-center">
				<div class="header-container">
					<lottie-player
						src="src/assets/images/lottiefiles/email.json"
						background="transparent"
						class="mx-auto"
						speed="1"
						style="width: 8rem; height: 8rem;"
						autoplay />
				</div>

				<h3 class="mb-0">
					Disposable Email Validator
				</h3>

				<p class="mb-4 text-secondary">
					<small>
						Validate disposable email address in seconds!
					</small>
				</p>

				<div class="mb-3">
					<form
						class="needs-validation"
						@submit.prevent>
						<div class="mb-3">
							<label class="form-label">
								Enter Email
							</label>
							
							<TheInput
								v-model="emailForm.email"
								placeholder="Enter email address"
								:disabled="isLoading"
								:class="{
									'is-invalid': v$.email.$error && v$.email.$dirty,
									'is-valid': !v$.email.$error && v$.email.$dirty
								}"
								@blur="v$.email.$touch" />
							<div
								v-for="error of v$.email.$errors"
								:key="error.$uid"
								class="invalid-feedback">
								{{ error.$message }}
							</div>
						</div>
					</form>

					<button
						v-if="!disposedEmailResult"
						class="btn btn-outline-primary mb-3"
						:disabled="isLoading || v$.$invalid"
						@click="validateEmail()">
						<span v-if="!isLoading">
							Verify
						</span>
						<span v-else>
							<i class="fa-solid fa-spinner fa-spin"></i>
						</span>
					</button>

					<div
						v-else
						class="d-grid gap-2 d-flex justify-content-center">
						<button
							class="btn btn-outline-primary"
							:disabled="isLoading"
							@click="reset()">
							Check again
						</button>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts">
import { computed, defineComponent, ref } from 'vue'

import useVuelidate from '@vuelidate/core'
import { email, helpers, required } from '@vuelidate/validators'

import { useServiceStore } from '@/store'
import TheInput from '@/components/forms/TheInput.vue'
import { TextConcat } from '@/helpers/typography'
import { useToastStore } from '@/store/modules/toast.module'
import type { DisposableEmailMeta } from '@/types/disposable-email-validator.models'

const VALIDATED_NOT_DISPOSABLE = 'The email <email> is valid and not disposable '
const VALIDATED_DISPOBABLE = 'Warning, the email <email> is a disposable email'
const VALIDATED_SERVER_ERROR = 'An error has occured, please try again later...'

export default defineComponent({
	name: 'EmailValidatorView',
	components: {
		TheInput
	},
	setup() {
		// Data
		const disposedEmailResult = ref<DisposableEmailMeta | null>(null)

		// Services
		const serviceSvc = useServiceStore()
		const toastr = useToastStore()

		//  Forms 
		const emailForm = ref({ email: null })
		const validation = {
			email: { 
				required: helpers.withMessage(
					'Need to have a value',
					required
				),
				email: helpers.withMessage(
					'Need to have a valid email',
					email
				)
			}
		}
		const v$ = useVuelidate(validation, emailForm)

		// Checkers
		const isLoading = ref<boolean>(false)

		// Validate Email
		const validateEmail = () => {
			if (v$.value.$invalid) return

			isLoading.value = true
			
			return serviceSvc.validateDisposableEmail(emailForm.value)
				.then(data => {
					disposedEmailResult.value = data.result
					isLoading.value = false

					if (!disposedEmailResult.value.disposable && disposedEmailResult.value.format) {
						toastr.success(validatedNotDisposableMsg.value)
					} else if (disposedEmailResult.value.disposable && disposedEmailResult.value.format) {
						toastr.warning(validatedDisposableMsg.value)
					} else if (disposedEmailResult.value.disposable && !disposedEmailResult.value.format) {
						toastr.warning(validatedServerErrorMsg.value)
					}
				})
				.catch(() => {
					isLoading.value = false
				})
		}

		// Reset form
		const reset = () => {
			emailForm.value.email = null
			disposedEmailResult.value = null
			v$.value.$reset()
		}

		const validatedNotDisposableMsg = computed(() => {
			const curEmail = emailForm.value.email ? emailForm.value.email : ''
			return (TextConcat(VALIDATED_NOT_DISPOSABLE, '<email>', curEmail))
		})

		const validatedDisposableMsg = computed(() => {
			const curEmail = emailForm.value.email ? emailForm.value.email : ''
			return (TextConcat(VALIDATED_DISPOBABLE, '<email>', curEmail))
		})

		const validatedServerErrorMsg = ref<string>(VALIDATED_SERVER_ERROR)

		return {
			emailForm,
			v$,
			disposedEmailResult,
			isLoading,
			validateEmail,
			reset,
			validatedNotDisposableMsg,
			validatedDisposableMsg,
			validatedServerErrorMsg
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

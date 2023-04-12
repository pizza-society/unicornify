<template>
	<div
		class="d-flex toast show fade mx-auto fixed-bottom bg-dark py-1 px-2"
		role="alert"
		aria-live="assertive"
		aria-atomic="true"
		style="bottom: 1rem;">
		<div
			class="d-inline-flex justify-content-center align-items-center
			flex-shrink-0 p-1 my-auto rounded"
			style="height: 1.5rem; width: 1.5rem; background-color: rgb(3 84 63);">
			<svg
				aria-hidden="true"
				class="w-5 h-5"
				fill="currentColor"
				viewBox="0 0 20 20"
				xmlns="http://www.w3.org/2000/svg">
				<path
					fill-rule="evenodd"
					d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
					clip-rule="evenodd" />
			</svg>
		</div>
		<div class="d-flex align-items-center py-2 ps-2 pe-2">
			Hello, world! This is a toast message.
		</div>
	</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
	name: 'TheSnackbar',
	props: {
		theme: {
			type: String as () => 'info' | 'success' | 'error' | 'warning',
			default: 'info'
		},
		text: {
			type: String,
			default: ''
		}
	},
	setup() {
		return {}
	}
})
</script>

<style lang="scss" scoped></style>
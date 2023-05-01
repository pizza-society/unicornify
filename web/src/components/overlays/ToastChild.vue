<template>
	<div
		class="d-flex toast show fade mx-auto bg-dark py-1 px-2 mb-2"
		role="alert"
		style="bottom: 1rem;">
		<div
			class="d-inline-flex justify-content-center align-items-center
			flex-shrink-0 p-1 my-auto rounded-circle toast-icon"
			:class="colorMapped">
			<i :class="iconMapped"></i>
		</div>
		<div class="d-flex align-items-center py-2 ps-2 pe-2 text">
			{{ text }}
		</div>
	</div>
</template>

<script lang="ts">
import { computed, defineComponent } from 'vue'

import { ToastColorMap, ToastIconMap, ToastType } from '@/types'

export default defineComponent({
	name: 'ToastChild',
	props: {
		theme: {
			type: String as () => ToastType,
			default: 'success'
		},
		text: {
			type: String,
			default: 'n/a'
		}
	},
	setup(props) {
		const iconMapped = computed<string>(() => {
			return ToastIconMap[props.theme]
		})

		const colorMapped = computed<string>(() => {
			return ToastColorMap[props.theme]
		})

		return {
			iconMapped,
			colorMapped
		}
	}
})
</script>

<style lang="scss" scoped>
.toast-icon {
	height: 1.3rem;
	width: 1.3rem;
}

.toast-info {
	background-color: rgb(30, 64, 175, 0.5);
}

.toast-success {
	background-color: rgb(22, 101, 52, 0.5);
}

.toast-warning {
	background-color: rgb(234, 179, 8, 0.5);
}

.toast-error {
	background-color: rgb(159, 18, 57, 0.5);
}
</style>
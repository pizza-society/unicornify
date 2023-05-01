<template>
	<input
		class="form-control"
		:class="$attrs.class"
		type="{{ $attrs.type }}"
		:value="modelValue" 
		@blur="$emit('blur')"
		@input="$emit('update:modelValue', ($event.target as HTMLInputElement).value)" />
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
	name: 'TheInput',
	props: {
		modelValue: {
			type: String as () => string | null | undefined,
			default: undefined
		},
		isLight: {
			type: Boolean,
			default: false
		}
	},
	emits: ['blur', 'update:modelValue'],
	setup() {
		return { }
	}
})
</script>

<style lang="scss" scoped>
</style>
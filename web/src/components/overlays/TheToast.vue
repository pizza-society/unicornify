<template>
	<div class="fixed-bottom py-2">
		<template 
			v-for="item of notificationList"
			:key="item.id">
			<ToastChild
				:text="item.text"
				:theme="item.theme" />
		</template>
	</div>
</template>

<script lang="ts">
import { computed, defineComponent } from 'vue'

import ToastChild from './ToastChild.vue'
import { ToastChildItem } from '@/types'
import { useToastStore } from '@/store'


export default defineComponent({
	name: 'TheToast',
	components: {
		ToastChild
	},
	setup() {
		const toastr = useToastStore()

		const notificationList = computed<ToastChildItem[]>(
			() => {
				return toastr.$state.notificationList
			}
		)
		return {
			notificationList
		}
	}
})
</script>

<style lang="scss" scoped></style>
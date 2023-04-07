<template>
	<div class="container py-3">
		<button
			type="button" 
			class="btn btn-primary mb-3"
			@:click="toggleModal()">
			Toggle modal
		</button>

		<button
			type="button" 
			class="btn btn-primary mb-3"
			@:click="generate()">
			Test pinia
		</button>

		<img
			v-if="generatedResult" 
			:src="`data:image/jpg;base64,${ generatedResult }`" />

		<ModalComponent ref="modalComponent">
			<template #header>
				<span>
					This is a title
				</span>
			</template>

			<template #content>
				<p class="mb-0">
					Hello here
				</p>
			</template>

			<template #footer>
				<button
					type="button"
					class="btn btn-secondary"
					@:click="toggleModal()">
					Close
				</button>
				
				<button
					type="button"
					class="btn btn-primary"
					@:click="toggleModal()">
					Save changes
				</button>
			</template>
		</ModalComponent>
		
		<AccordionComponent ref="accordionComponent" />
	</div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

import ModalComponent from '@/components/ModalComponent.vue'
import AccordionComponent from '@/components/AccordionComponent.vue'
import { useServiceStore } from '@/store'

export default defineComponent({
	name: 'TestingView',
	components: {
		AccordionComponent,
		ModalComponent
	},
	setup() {
		const modalComponent = ref<InstanceType<typeof ModalComponent>>()
		const accordionComponent = ref<InstanceType<typeof AccordionComponent>>()
		const generatedResult = ref<string | null | unknown>(null)
		const serviceSvc = useServiceStore()

		const toggleModal = () => {
			modalComponent.value?.toggleModal()
		}

		const generate = () => {
			return serviceSvc.generateQR({
				'link': 'https://google.com'
			}).then(data => {
				generatedResult.value = data
			})
		}

		return {
			modalComponent,
			accordionComponent,
			toggleModal,
			generate,
			generatedResult
		}
	}
})
</script>

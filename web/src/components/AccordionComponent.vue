<template>
	<div>
		<div class="accordion">
			<div class="accordion-item">
				<h2 class="accordion-header">
					<button
						class="accordion-button"
						type="button"
						:class="{
							'collapsed': !isAccordionOpen[0]
						}"
						@click="toggleItem(0)">
						Accordion Item #1
					</button>
				</h2>
				<Transition>
					<div
						class="accordion-collapse collapse"
						:class="{
							'show': isAccordionOpen[0]
						}">
						<div class="accordion-body">
							<strong>This is the first item's accordion body.</strong>
							It is shown by default, until the collapse plugin adds
							the appropriate classes that we use to style each
							element. These classes control the overall appearance,
							as well as the showing and hiding via CSS transitions.
							You can modify any of this with custom CSS or overriding
							our default variables. It's also worth noting that just
							about any HTML can go within the
							<code>.accordion-body</code>, though the transition does
							limit overflow.
						</div>
					</div>
				</Transition>
			</div>

			<div class="accordion-item">
				<h2 class="accordion-header">
					<button
						class="accordion-button"
						type="button"
						:class="{
							'collapsed': !isAccordionOpen[1]
						}"
						@click="toggleItem(1)">
						Accordion Item #2
					</button>
				</h2>
				<div
					class="accordion-collapse collapse"
					:class="{
						'show': isAccordionOpen[1]
					}">
					<div class="accordion-body">
						<strong>This is the second item's accordion body.</strong>
						It is hidden by default, until the collapse plugin adds
						the appropriate classes that we use to style each
						element. These classes control the overall appearance,
						as well as the showing and hiding via CSS transitions.
						You can modify any of this with custom CSS or overriding
						our default variables. It's also worth noting that just
						about any HTML can go within the
						<code>.accordion-body</code>, though the transition does
						limit overflow.
					</div>
				</div>
			</div>
			<div class="accordion-item">
				<h2 class="accordion-header">
					<button
						class="accordion-button"
						type="button"
						:class="{
							'collapsed': !isAccordionOpen[2]
						}"
						@click="toggleItem(2)">
						Accordion Item #3
					</button>
				</h2>
				<div
					class="accordion-collapse collapse"
					:class="{
						'show': isAccordionOpen[2]
					}">
					<div class="accordion-body">
						<strong>This is the third item's accordion body.</strong>
						It is hidden by default, until the collapse plugin adds
						the appropriate classes that we use to style each
						element. These classes control the overall appearance,
						as well as the showing and hiding via CSS transitions.
						You can modify any of this with custom CSS or overriding
						our default variables. It's also worth noting that just
						about any HTML can go within the
						<code>.accordion-body</code>, though the transition does
						limit overflow.
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

export default defineComponent({
	name: 'AccordionComponent',
	setup() {
		const isAccordionOpen = ref<boolean[]>([false, true, false])

		const toggleItem = (index: number) => {
			return isAccordionOpen.value[index] = !isAccordionOpen.value[index]
		}

		return {
			isAccordionOpen,
			toggleItem
		}
	}
})
</script>

<style lang="scss">
	.v-enter-active,
	.v-leave-active {
		transition: opacity 0.2s ease;
	}

	.v-enter-from,
	.v-leave-to {
		opacity: 0;
	}
</style>
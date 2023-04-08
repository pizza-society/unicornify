<template>
	<div class="navbar-nav">
		<template
			v-for="item in items"
			:key="item.path">
			<template v-if="item.path && !item.dropdown">
				<router-link
					class="nav-link"
					:to="item.path"
					active-class="active text-primary">
					{{ item.title }}
				</router-link>
			</template>

			<template v-else-if="!item.path && item.dropdown">
				<li
					class="nav-item nav-item-dropdown dropdown"
					@mouseover="toggleDropdownMenu(item.name)"
					@mouseleave="toggleDropdownMenu('')">
					<a
						class="nav-link dropdown-toggle mt-0"
						data-bs-toggle="dropdown"
						role="button"
						:aria-expanded="currentToggledMenu === item.name ? 'true' : 'false'"
						:class="{
							'show': currentToggledMenu === item.name
						}">
						{{ item.title }}
					</a>

					<ul
						class="dropdown-menu"
						:class="{
							'show': currentToggledMenu === item.name
						}"
						@mouseover="toggleDropdownMenu(item.name)"
						@mouseleave="toggleDropdownMenu('')">
						<template 
							v-for="dropItem in item.dropdown"
							:key="dropItem.path">
							<li class="dropdown-item-parent">
								<router-link
									class="dropdown-item rounded"
									:to="dropItem.path"
									active-class="active text-primary">
									{{ dropItem.title }}
								</router-link>
							</li>
						</template>
					</ul>
				</li>
			</template>
		</template>
	</div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

import { NavbarItem } from '@/common/navbar'

export default defineComponent({
	name: 'NavbarNav',
	props: {
		items: {
			type: Array as () => NavbarItem[],
			default: () => {
				return []
			}
		}
	},
	setup() {
		const currentToggledMenu = ref<string>('')
		const toggleDropdownMenu = (menuName: string) => {
			return currentToggledMenu.value === menuName ?
				currentToggledMenu.value = '' :
				currentToggledMenu.value = menuName
		}

		return { 
			toggleDropdownMenu,
			currentToggledMenu
		}
	}
})
</script>

<style lang="scss" scoped>

.nav-item-dropdown {
	.dropdown-menu {
		padding: 0.65rem;
		.dropdown-item-parent:not(:last-child) .dropdown-item {
			margin-bottom: 0.25rem;
		}

		.dropdown-item-parent .dropdown-item.active {
			background-color: transparent;
			transition: background-color 0.15s ease-in-out, color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
			-moz-transition: background-color 0.15s ease-in-out, color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
		}

		.dropdown-item-parent .dropdown-item:not(.active) {
			// color: rgba(255, 255, 255, 0.55);
			transition: background-color 0.15s ease-in-out, color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
			-moz-transition: background-color 0.15s ease-in-out, color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
		}
	}
}
</style>
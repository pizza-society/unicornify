<template>
	<div class="navbar-nav">
		<template
			v-for="item in items"
			:key="item.path">
			<template v-if="item.path && !item.dropdown">
				<router-link
					class="nav-link"
					:to="item.path"
					active-class="active text-primary"
					@click.self="emitMobile()">
					{{ item.title }}
				</router-link>
			</template>

			<template v-else-if="!item.path && item.dropdown">
				<li
					class="nav-item nav-item-dropdown dropdown"
					@mouseover="toggleDropdownMenu(item.name)"
					@mouseleave="toggleDropdownMenu('')">
					<a
						class="nav-link dropdown-toggle mt-0 d-flex d-sm-block"
						role="button"
						:aria-expanded="currentToggledMenu === item.name ? 'true' : 'false'"
						:class="{
							'show': currentToggledMenu === item.name
						}"
						@click="toggleDropdownMenu(item.name)">
						{{ item.title }}
						<i class="fa-solid fa-plus fa-xs d-block d-md-none"></i>
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
									active-class="active text-primary"
									@click.self="emitMobile()">
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
import { computed, defineComponent, ref } from 'vue'

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
	emits: [
		'onMobileClick'
	],
	setup(props, context) {
		const currentToggledMenu = ref<string>('')
		const toggleDropdownMenu = (menuName: string) => {
			console.log('heheh')
			return currentToggledMenu.value === menuName ?
				currentToggledMenu.value = '' :
				currentToggledMenu.value = menuName
		}

		const isMobile = computed(() => {
			return (/iphone|ipod|android|ie|blackberry|fennec/).test(navigator.userAgent.toLowerCase())
		})

		const emitMobile = () => {
			// emit on mobile click to toggle menu
			// on mobile after an action
			if (isMobile.value) {
				context.emit('onMobileClick')
			}
		}

		return { 
			toggleDropdownMenu,
			currentToggledMenu,
			emitMobile
		}
	}
})
</script>

<style lang="scss" scoped>
@media (max-width: 576px) {
	.navbar-nav .nav-link {
		padding: 0.69rem 0 !important;
	}
	

	.nav-link.dropdown-toggle::after {
		display: none;
	}

	.dropdown-toggle {
		justify-content: space-between;
		align-items: center;
	}

	.nav-item-dropdown {
		.dropdown-menu {
			--bs-dropdown-border-color: none;
			--bs-dropdown-bg: transparent;
			--bs-dropdown-box-shadow: transparent;
			border-radius: 0;
			padding: 0.69rem 0;
			
			.dropdown-item-parent .dropdown-item {
				--bs-dropdown-link-active-bg: transparent;
				--bs-dropdown-link-active-color: #ffffff80;
				padding-top: 0;
				padding-bottom: 0;
				padding-left: 0.3rem;
			}
			&:last-child {
				border-bottom: 1px solid #343a40;
			}
		}
	}
}

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
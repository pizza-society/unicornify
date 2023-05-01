<template>
	<div class="container">
		<div class="d-flex flex-row vh-min justify-content-center align-items-center row">
			<div class="col-md-5">
				<img
					src="@/assets/images/outer-space.svg"
					style="height: auto; width: 100%"
					class="mx-auto" />
			</div>
			
			<div class="col-md-4">
				<div class="my-auto text-center">
					<img
						src="@/assets/images/unicornify-banner-white.png"
						style="height: auto; width: 100%"
						class="mx-auto" />

					<p class="small">
						Version: v{{ appVersion }}
					</p>

					<div class="d-grid gap-2 d-flex justify-content-center my-2">
						<a
							class="btn btn-outline-primary github-desktop"
							href="https://github.com/syfqpie"
							target="_blank">
							<i class="fa-brands fa-github"></i>
							sb
						</a>
						<a
							class="btn btn-outline-primary github-desktop"
							href="https://github.com/Dev-R"
							target="_blank">
							<i class="fa-brands fa-github"></i>
							rabee
						</a>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

export default defineComponent({
	name: 'AboutView',
	setup() {
		const appVersion = ref<string>(import.meta.env.VITE_UNICORNIFY_VERSION)

		return { appVersion }
	}
})
</script>
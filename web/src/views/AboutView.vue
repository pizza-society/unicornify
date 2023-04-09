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
				<div class="my-auto">
					<iframe
						width="auto"
						src="https://www.youtube.com/embed/_TyInMXIgUE?autoplay=1"
						title="YouTube video player"
						frameborder="0"
						allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture">
					</iframe>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
	name: 'AboutView',
	setup() {
		return {}
	}
})
</script>
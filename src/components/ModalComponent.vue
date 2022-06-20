<template>
	<div>
		<Transition>
			<div class="modal fade show d-block"
				v-if="isModalOpen">
				<div class="modal-dialog modal-dialog-centered">
					<div class="modal-content bg-dark">
						<div class="modal-header">
							<h5 class="modal-title">
								<slot name="header" />
							</h5>
							<button
								type="button"
								class="btn-close rounded-circle"
								v-on:click="toggleModal()">
							</button>
						</div>
						<div class="modal-body">
							<slot name="content" />
						</div>
						<div class="modal-footer">
							<slot name="footer" />
						</div>
					</div>
				</div>
			</div>
		</Transition>
		<div class="modal-backdrop fade show" v-if="isModalOpen"></div>
	</div>
</template>

<script lang="ts">
import { onMounted, defineComponent, ref } from "vue";

export default defineComponent({
    name: "ModalComponent",
    setup() {
        const isModalOpen = ref<boolean>(false);

        const toggleModal = () => {
            return (isModalOpen.value = !isModalOpen.value);
        };

        onMounted(() => {
            console.log("modalComponent");
        });

        return {
            isModalOpen,
            toggleModal,
        };
    },
});
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
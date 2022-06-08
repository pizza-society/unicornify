<template>
    <div class="modal fade"
        :class="{
            'show d-block': isModalOpen
        }">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content bg-dark">
                <div class="modal-header border-dark">
                    <h5 class="modal-title">
                        <slot name="header" />
                    </h5>
                    <button type="button"
                        class="btn-close"
                        v-on:click="toggleModal()">
                    </button>
                </div>
                <div class="modal-body">
                    <slot name="content" />
                </div>
                <div class="modal-footer border-dark">
                    <slot name="footer" />
                </div>
            </div>
        </div>
    </div>

    <div class="modal-backdrop fade show" v-if="isModalOpen"></div>
</template>

<script lang="ts">
import { onMounted, defineComponent, ref } from 'vue';

export default defineComponent({
  name: 'ModalBase',
  setup() {
    const isModalOpen = ref<boolean>(false)

    const toggleModal = () => {
      return isModalOpen.value = !isModalOpen.value
    }

    onMounted(() => {
      console.log('modalComponent')
    })

    return {
      isModalOpen,
      toggleModal
    }
  }
})

</script>

<style lang="scss" scoped>

</style>
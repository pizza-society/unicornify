<template>
    <div class="container py-3">
        <button type="button" 
            class="btn btn-primary"
            v-on:click="toggleModal()">
            Toggle modal
        </button>

        <ModalComponent ref="modalComponent">
            <template #header>
                <span>
                    This is a title
                </span>
            </template>

            <template #content>
                <p class="mb-0">Hello here</p>
            </template>

            <template #footer>
                <button type="button"
                    class="btn btn-secondary"
                    v-on:click="toggleModal()">
                    Close
                </button>
                <button type="button"
                    class="btn btn-primary"
                    v-on:click="toggleModal()">
                    Save changes
                </button>
            </template>
        </ModalComponent>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import ModalComponent from '@/components/ModalComponent.vue';

export default defineComponent({
    name: 'TestingView',
    setup() {
        const modalComponent = ref<InstanceType<typeof ModalComponent>>()

        const toggleModal = () => {
            modalComponent.value?.toggleModal()
        }

        return {
            modalComponent,
            toggleModal
        }
    },
    components: {
        ModalComponent
    }
})
</script>

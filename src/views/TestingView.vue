<template>
    <div class="container py-3">
        <button type="button" 
            class="btn btn-primary mb-3"
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
        <AccordionComponent ref="accordionComponent"></AccordionComponent>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import ModalComponent from '@/components/ModalComponent.vue';
import AccordionComponent from '@/components/AccordionComponent.vue';

export default defineComponent({
    name: 'TestingView',
    setup() {
        const modalComponent = ref<InstanceType<typeof ModalComponent>>()
        const accordionComponent = ref<InstanceType<typeof AccordionComponent>>()

        const toggleModal = () => {
            modalComponent.value?.toggleModal()
        }

        return {
            modalComponent,
            accordionComponent,
            toggleModal
        }
    },
    components: {
        ModalComponent,
        AccordionComponent
    }
})
</script>

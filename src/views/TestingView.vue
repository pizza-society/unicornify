<template>
    <div>
        <button type="button" 
            class="btn btn-primary"
            v-on:click="toggleModal()">
            Toggle modal
        </button>

        <ModalBase ref="modalComponent">
            <template #header>
                <span>
                    This is a title
                </span>
            </template>

            <template #content>
                <p>Hello here</p>
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
        </ModalBase>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import ModalBase from '@/components/modals/ModalBase.vue';

export default defineComponent({
    name: 'TestingView',
    setup() {
        const modalComponent = ref<InstanceType<typeof ModalBase>>()

        const toggleModal = () => {
            modalComponent.value?.toggleModal()
        }

        return {
            modalComponent,
            toggleModal
        }
    },
    components: {
        ModalBase
    }
})
</script>

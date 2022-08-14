import { shallowMount } from '@vue/test-utils'
import QRGeneratorView from '@/views/QRGeneratorView.vue'
import { setActivePinia, createPinia } from 'pinia'
import { createTestingPinia } from '@pinia/testing'

describe('QRGeneratorView.vue', () => {
  beforeEach(() => {
    // creates a fresh pinia and make it active so it's automatically picked
    // up by any useStore() call without having to pass it to it:
    // `useStore(pinia)`
    // setActivePinia(createPinia())
  })
  it('renders props.msg when passed', () => {
    const msg = 'QR Generator  Generate your own QR code with customized design! Enter URL Generate  Design'
    const wrapper = shallowMount(QRGeneratorView, {
      props: { msg },
      global: {
        plugins: [createTestingPinia()],
      }
    })
    expect(wrapper.text()).toMatch(msg)
  })
})

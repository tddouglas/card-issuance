<template>
	<the-dropdown
		:dropdown-options="addressOptions"
		class="my-8"
		@set="setAddress">
		<template #dropdown-text>Select Shipping Address</template>
	</the-dropdown>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import TheDropdown from '@/components/TheDropdown.vue'
import { mapStores } from 'pinia'
import { newCardOrderStore } from '@/stores/newCardOrder'

export default defineComponent({
	name: 'NewOrderShippingAddressSelection',
	components: { TheDropdown },
	computed: {
		...mapStores(newCardOrderStore)
	},
	methods: {
		setAddress(address: string) {
			this.newCardOrderStore.selectedAddress = address
		},
	},
	data() {
		return {
			// TODO: Add country and postal codes. Full addresses here - https://www.adyen.com/offices
			addressOptions: ['Simon Carmiggeltstraat 6-50', 'Rokin 49', '71 5th Avenue, 11th Floor'],
		}
	},
})
</script>
<template>
	<div class="mb-8 text-xl">
		Please Provide {{ newCardOrderStore.selectedCountry }}
		{{ newCardOrderStore.selectedOrderType }} Event Details Below:
	</div>
	<div class="grid grid-cols-3">
		<span class="pt-1">Number of Cards:</span>
		<the-input-number
			label-text="Number of Cards"
			class="h-10 sm:w-72 mb-8 col-span-2"
			@set="setNumberOfCards"></the-input-number>
		<span class="pt-1">Start Date:</span>
		<the-input-date
			class="h-10 sm:w-72 col-span-2 mb-8"
			@set="setStartDate"></the-input-date>
		<span class="pt-1">End Date:</span>
		<the-input-date
			class="h-10 sm:w-72 col-span-2"
			@set="setEndDate"></the-input-date>
	</div>
	<new-order-card-art-selection></new-order-card-art-selection>
	<new-order-shipping-address-selection></new-order-shipping-address-selection>
	<div v-if="orderEventDetailsValid()" class="mt-8">
		<the-button
			reference="submitButton"
			:focus="focusSubmit"
			@click="submitOrder">
			<template #button-text>Confirm Card Order</template>
		</the-button>
	</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import TheInputNumber from '@/components/TheInputNumber.vue'
import TheInputDate from '@/components/TheInputDate.vue'
import TheButton from '@/components/TheButton.vue'
import NewOrderCardArtSelection from '@/components/newOrder/newOrderCardArtSelection.vue'
import { mapStores } from 'pinia'
import { newCardOrderStore } from '@/stores/newCardOrder'
import NewOrderShippingAddressSelection from '@/components/newOrder/newOrderShippingAddressSelection.vue'

export default defineComponent({
	name: 'NewOrderEventDetails',
	components: {
		NewOrderShippingAddressSelection,
		TheButton,
		TheInputNumber,
		TheInputDate,
		NewOrderCardArtSelection,
	},
	computed: {
		...mapStores(newCardOrderStore),
	},
	methods: {
		orderEventDetailsValid(): boolean {
			return (
				this.newCardOrderStore.numberOfCards > 0 &&
				this.newCardOrderStore.eventStartDate.length > 0 &&
				this.newCardOrderStore.eventEndDate.length > 0 &&
				this.newCardOrderStore.selectedImage.length > 0 &&
				this.newCardOrderStore.selectedAddress.length > 0
			)
		},
		setNumberOfCards(numberOfCards: number) {
			this.newCardOrderStore.numberOfCards = numberOfCards
		},
		setStartDate(eventStartDate: string) {
			this.newCardOrderStore.eventStartDate = eventStartDate
		},
		setEndDate(eventEndDate: string) {
			this.newCardOrderStore.eventEndDate = eventEndDate
		},
		async submitOrder() {
			try {
				// TODO: Tied to backend to actually submit order
				// const res = await fetch('http://localhost:8000', {
				// 	method: 'POST',
				// 	body: JSON.stringify({}),
				// })
				if (true) {
					console.log('Order successfully submitted')
					this.$router.push({
						path: '/orderSubmissionResult',
						query: { success: 'true' },
					})
				}
			} catch (e) {
				console.error(e)
			}
		},
	},
	mounted() {
		this.newCardOrderStore.resetOrderDetails()
	},
	data() {
		return {
			focusSubmit: false,
		}
	},
})
</script>

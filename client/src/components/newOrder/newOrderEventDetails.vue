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
	<new-order-shipping-address-selection></new-order-shipping-address-selection>
	<new-order-card-art-selection></new-order-card-art-selection>
	<div v-if="newCardOrderStore.isOrderEventDetailsValid" class="mt-8">
		<the-button
			reference="submitButton"
			:loading="orderSubmitLoading"
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
import NewOrderShippingAddressSelection from '@/components/newOrder/newOrderShippingAddressSelection.vue'
import NewOrderCardArtSelection from '@/components/newOrder/newOrderCardArtSelection.vue'
import TheButton from '@/components/TheButton.vue'
import { mapStores } from 'pinia'
import { newCardOrderStore } from '@/stores/newCardOrder'
import { postBackend } from '@/helpers/fetchUtil'

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
	watch: {
		'newCardOrderStore.isOrderEventDetailsValid'() {
			if (this.newCardOrderStore.isOrderEventDetailsValid) {
				this.focusSubmit = true
			}
		},
	},
	methods: {
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
			this.orderSubmitLoading = true
			const body = this.newCardOrderStore.getNewCardOrderObject
			const res = await postBackend('new_order', body)
			if (res) {
				console.log('Order successfully submitted')
				this.$router.push({
					path: '/orderSubmissionResult',
					query: { success: 'true' },
				})
			}
		},
	},
	mounted() {
		this.newCardOrderStore.resetOrderDetails()
	},
	data() {
		return {
			orderSubmitLoading: false,
			focusSubmit: false,
		}
	},
})
</script>

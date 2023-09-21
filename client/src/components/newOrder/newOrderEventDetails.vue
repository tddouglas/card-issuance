<template>
	<div class="my-8 text-xl">Please Provide Event Details Below</div>
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
	<the-dropdown
		:dropdown-options="cardOrderImageOptions"
		class="my-8"
		@set="setImage">
		<template #dropdown-text>Select Image to use on card</template>
	</the-dropdown>
	<div v-if="orderEventDetailsValid()">
		<the-button @click="submitOrder">
			<template #button-text>Confirm Card Order</template>
		</the-button>
	</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import TheInputNumber from '@/components/TheInputNumber.vue'
import TheInputDate from '@/components/TheInputDate.vue'
import TheDropdown from '@/components/TheDropdown.vue'
import { mapStores } from 'pinia'
import { newCardOrderStore } from '@/stores/newCardOrder'
import TheButton from '@/components/TheButton.vue'

export default defineComponent({
	name: 'NewOrderEventDetails',
	components: { TheButton, TheDropdown, TheInputNumber, TheInputDate },
	computed: {
		...mapStores(newCardOrderStore),
	},
	methods: {
		orderEventDetailsValid(): boolean {
			return (
				this.newCardOrderStore.numberOfCards > 0 &&
				this.newCardOrderStore.eventStartDate &&
				this.newCardOrderStore.eventEndDate &&
				this.newCardOrderStore.selectedImage
			)
		},
		setNumberOfCards(numberOfCards: number) {
			console.log('setting numOfCards', numberOfCards)
			this.newCardOrderStore.numberOfCards = numberOfCards
		},
		setStartDate(eventStartDate: string) {
			this.newCardOrderStore.eventStartDate = eventStartDate
		},
		setEndDate(eventEndDate: string) {
			this.newCardOrderStore.eventEndDate = eventEndDate
		},
		setImage(image: string) {
			this.newCardOrderStore.selectedImage = image
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
						query: { success: true },
					})
				}
			} catch (e) {
				console.error(e)
			}
		},
	},
	data() {
		return {
			// TODO: Surface proper Image options. Ideally render in browser
			cardOrderImageOptions: ['IM1236178924612012', 'IM87566171273489'],
		}
	},
})
</script>

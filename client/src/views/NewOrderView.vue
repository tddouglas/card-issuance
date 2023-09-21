<template>
	<div
		class="flex justify-center items-center flex-col">
		<the-dropdown
			:dropdown-options="cardOrderCountries"
			class="mb-8"
			@set="setCountry">
			<template #dropdown-text
				>Select Country where cards will be used
			</template>
		</the-dropdown>
		<the-dropdown :dropdown-options="cardOrderTypes" @set="setOrderType">
			<template #dropdown-text>Select Card Order Type</template>
		</the-dropdown>
		<div v-if="showProgram()">
			<div class="mt-8 flex flex-col items-center">
				<div class="my-8 text-xl">
					The program you have selected has the following pre-approved
					spend limits:
				</div>
				<the-grid
					:rows="tableRows"
					:headers="tableHeaders"
					class="opacity-70"></the-grid>
				<div class="flex flex-row mt-10">
					<the-button
						class="w-48 h-12 mr-10"
						@click="setSpendLimitsApproved">
						<template #button-text>Approve Limits</template>
					</the-button>
					<router-link to="/requestNewLimits">
						<the-button class="w-48 h-12">
							<template #button-text>Request New Limits</template>
						</the-button>
					</router-link>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import TheDropdown from '@/components/TheDropdown.vue'
import TheButton from '@/components/TheButton.vue'
import TheGrid from '@/components/TheGrid.vue'
import NewOrderEventDetails from '@/components/newOrder/newOrderEventDetails.vue'
import { mapStores } from 'pinia'
import { newCardOrderStore } from '@/stores/newCardOrder'

export default defineComponent({
	name: 'NewOrderView',
	components: { TheDropdown, TheButton, TheGrid },
	computed: {
		...mapStores(newCardOrderStore),
	},
	methods: {
		setSpendLimitsApproved() {
			this.$router.push('/newCardOrderDetails')
		},
		setCountry(country: string) {
			this.newCardOrderStore.selectedCountry = country
		},
		setOrderType(orderType: string) {
			this.newCardOrderStore.selectedOrderType = orderType
		},
		showProgram() {
			return (
				this.newCardOrderStore.selectedCountry &&
				this.newCardOrderStore.selectedOrderType
			)
		},
	},
	data() {
		return {
			spendLimitsApproved: false,
			cardOrderCountries: ['US', 'UK', 'NL'],
			cardOrderTypes: ['Internal Event', 'Recruiting'],
			tableHeaders: [
				'Daily Spend Limit',
				'Max Transaction Amount',
				'Allowed Countries',
				'Allowed MCCs',
			],
			tableRows: [['€50.00', '€10.00', 'EU & UK', 'All MCCs']],
		}
	},
})
</script>

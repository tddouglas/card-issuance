<template>
	<div class="flex justify-center items-center flex-col">
		<the-dropdown
			:dropdown-options="usecaseStore.getUniqueCountries()"
			class="mb-8"
			@set="setCountry">
			<template #dropdown-text
				>Select Country where cards will be used
			</template>
		</the-dropdown>
		<the-dropdown
			v-if="newCardOrderStore.isCountrySet"
			:dropdown-options="usecaseStore.getUniqueEventTypes()"
			@set="setOrderType">
			<template #dropdown-text>Select Card Order Type</template>
		</the-dropdown>
		<div v-if="newCardOrderStore.isMainOrderSet">
			<div class="mt-8 flex flex-col items-center">
				<div class="my-8 text-xl">
					The program you have selected has the following pre-approved
					spend limits:
				</div>
				<the-grid
					:rows="formatRows()"
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
import { mapStores } from 'pinia'
import { newCardOrderStore } from '@/stores/newCardOrder'
import { usecaseStore } from '@/stores/usecaseStore'
import { formatAmount } from '@/helpers/amountFormatter'

export default defineComponent({
	name: 'NewOrderView',
	components: { TheDropdown, TheButton, TheGrid },
	computed: {
		...mapStores(newCardOrderStore),
		...mapStores(usecaseStore),
	},
	methods: {
		setSpendLimitsApproved() {
			this.$router.push('/newCardOrderDetails')
		},
		setCountry(country: string) {
			if (this.newCardOrderStore.selectedCountry != country) {
				this.newCardOrderStore.selectedOrderType = '' // Reset selectedOrderType if changing country
			}
			this.newCardOrderStore.selectedCountry = country
		},
		setOrderType(orderType: string) {
			this.newCardOrderStore.selectedOrderType = orderType
		},
		formatRows(): Array<Array<string>> {
			// TODO: select the proper row. Right now hardcoded to 0
			if (this.usecaseStore.approvedUsecases.length > 0) {
				const unformattedRow = this.usecaseStore.approvedUsecases[1]
				const currency = unformattedRow['currency']
				const maxDailySpend = formatAmount(
					unformattedRow['max_daily_spend'],
					currency
				)
				const maxPerTransactionAmount = formatAmount(
					unformattedRow['max_amount_per_transaction'],
					currency
				)
				const allowedCountries = unformattedRow['allowed_countries']
				const allowedMCCs = unformattedRow['allowed_mccs']
				return [
					[
						maxDailySpend,
						maxPerTransactionAmount,
						allowedCountries,
						allowedMCCs,
					],
				]
			} else {
				return [[]]
			}
		},
	},
	async mounted() {
		this.newCardOrderStore.resetMainOrder()
		await this.usecaseStore.getApprovedUsecases()
	},
	data() {
		return {
			spendLimitsApproved: false,
			tableHeaders: [
				'Daily Spend Limit',
				'Max Transaction Amount',
				'Allowed Countries',
				'Allowed MCCs',
			],
		}
	},
})
</script>
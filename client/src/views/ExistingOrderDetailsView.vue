<template>
	<div>
		<div v-if="!existingCardOrderStore.isSelectedOrderEmpty">
			<table class="table-auto">
				<thead>
					<tr class="border-b">
						<th
							v-for="header in tableHeaders"
							:key="header"
							class="pb-2 text-left pr-8">
							{{ header }}
						</th>
					</tr>
				</thead>
				<tbody>
					<tr
						v-for="(
							row, index
						) in existingCardOrderStore.formatSelectedOrderCards"
						:key="index">
						<td
							v-for="(cell, index) in row"
							:key="cell"
							class="pt-2 min-w-[150px] pr-8">
							<card-order-status-circle
								v-if="index == 0"
								radius="20"
								:status="cell">
							</card-order-status-circle>
							{{ cell }}
						</td>
					</tr>
				</tbody>
			</table>
		</div>
		<div v-else>
			<h1>No Existing Orders</h1>
		</div>
	</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import CardOrderStatusCircle from '@/components/existingOrder/CardOrderStatusCircle.vue'
import { mapStores } from 'pinia'
import { existingCardOrderStore } from '@/stores/existingCardOrderStore'

export default defineComponent({
	name: 'ExistingOrderDetailsView',
	components: { CardOrderStatusCircle },
	computed: {
		...mapStores(existingCardOrderStore),
	},
	mounted() {
		const orderId = this.$route.params.id as string
		this.existingCardOrderStore.setSelectedOrderCards(orderId)
	},
	data() {
		return {
			tableHeaders: [
				'Card Status',
				'Payment Instrument ID',
				'Cardholder Name',
			],
		}
	},
})
</script>
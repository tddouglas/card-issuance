<template>
	<div>
		<div v-if="userOrders.length > 0">
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
					<tr v-for="(row, index) in tableRows" :key="index">
						<td
							v-for="cell in row"
							:key="cell"
							class="pt-2 min-w-[150px]">
							<card-order-status-circle
								v-if="cell == 'Shipped'"
								radius="20">
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
import type CardOrderItem from '@/types/cardOrderItem'
import CardOrderStatus from '@/types/cardOrderStatus'
import CardOrderStatusCircle from '@/components/existingOrder/CardOrderStatusCircle.vue'

export default defineComponent({
	name: 'ExistingOrderDetailsView',
	components: { CardOrderStatusCircle },
	methods: {},
	mounted() {
		this.userOrders = [
			{
				numberOfCards: 2,
				program: 'Recruiting',
			},
		]
	},
	data() {
		return {
			userOrders: [] as CardOrderItem[],
			tableHeaders: [
				'Card Status',
				'Cardholder Name',
				'Event Start',
				'Event End',
			],
			tableRows: [
				[
					CardOrderStatus.SHIPPED,
					'NA Recruiting0',
					'05-10-2023',
					'05-11-2023',
				],
				[
					CardOrderStatus.SHIPPED,
					'NA Recruiting1',
					'05-10-2023',
					'05-11-2023',
				],
				[
					CardOrderStatus.SHIPPED,
					'NA Recruiting2',
					'05-10-2023',
					'05-11-2023',
				],
				[
					CardOrderStatus.SHIPPED,
					'NA Recruiting3',
					'05-10-2023',
					'05-11-2023',
				],
			],
		}
	},
})
</script>

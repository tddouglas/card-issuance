<template>
	<div>
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
						row, i
					) in existingCardOrderStore.formatExistingCardOrders"
					:key="i">
					<td
						v-for="(cell, index) in row"
						:key="index"
						class="pt-2 pr-8">
						<router-link
							v-if="index == 0"
							:to="`/existingCardOrder/${cell.id}`"
							class="underline">
							{{ cell.cardOrderId }}
						</router-link>
						<div v-else>
							{{ cell }}
						</div>
					</td>
				</tr>
			</tbody>
		</table>
	</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { CardOrderStatus } from '@/types/cardOrderStatus'
import { EventType } from '@/types/eventType'
import { mapStores } from 'pinia'
import { existingCardOrderStore } from '@/stores/existingCardOrderStore'

export default defineComponent({
	name: 'ExistingOrderGrid',
	computed: {
		...mapStores(existingCardOrderStore),
	},
	data() {
		return {
			tableHeaders: [
				'Card Order ID',
				'Number of Cards',
				'Status',
				'Event Type',
			]
		}
	},
})
</script>

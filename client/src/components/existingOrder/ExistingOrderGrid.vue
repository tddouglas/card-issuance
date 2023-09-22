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
				<tr v-for="(row, i) in tableRows" :key="i">
					<td
						v-for="(cell, index) in row"
						:key="cell"
						class="pt-2 pr-8">
						<router-link
							v-if="index == 0"
							:to="`/existingCardOrder/${cell}`"
							class="underline">
							{{ cell }}
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
import { defineComponent, type PropType } from 'vue'
import CardOrderStatus from '@/types/cardOrderStatus'
import EventType from '@/types/eventType'

export default defineComponent({
	name: 'ExistingOrderGrid',
	data() {
		return {
			tableHeaders: [
				'Card Order ID',
				'Number of Cards',
				'Status',
				'Event Type',
			],
			tableRows: [
				[
					'CO3229G2232Z595HXX9R35GND',
					'20',
					CardOrderStatus.CREATED,
					EventType.INTERNAL,
				],
				[
					'CO3229G223264L5HT6SGTF3QZ',
					'10',
					CardOrderStatus.SHIPPED,
					EventType.RECRUITING,
				],
			],
		}
	},
})
</script>

<template>
	<div>
		<div v-if="existingCardOrderStore.exisingCardOrders.length > 0">
			<existing-orders-grid></existing-orders-grid>
		</div>
		<div v-else>
			<h1>No Existing Orders</h1>
		</div>
	</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import ExistingOrdersGrid from '@/components/existingOrder/ExistingOrderGrid.vue'
import { mapStores } from 'pinia'
import { existingCardOrderStore } from '@/stores/existingCardOrderStore'

export default defineComponent({
	name: 'ExistingOrderView',
	components: { ExistingOrdersGrid },
	computed: {
		...mapStores(existingCardOrderStore),
	},
	methods: {},
	async mounted() {
		await this.existingCardOrderStore.setExistingCardOrders()
	},
	data() {
		return {
		}
	},
})
</script>
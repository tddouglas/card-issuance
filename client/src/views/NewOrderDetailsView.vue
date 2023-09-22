<template>
	<div v-if="newCardOrderStore.isMainOrderSet" class="flex justify-center items-center flex-col">
		<new-order-event-details></new-order-event-details>
	</div>
	<div v-else>
		Please fill out Country and Card Order Type on previous page
	</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import NewOrderEventDetails from '@/components/newOrder/newOrderEventDetails.vue'
import { mapStores } from 'pinia'
import { newCardOrderStore } from '@/stores/newCardOrder'

export default defineComponent({
	name: 'NewOrderView',
	components: { NewOrderEventDetails },
	computed: {
		...mapStores(newCardOrderStore)
	},
})
</script>

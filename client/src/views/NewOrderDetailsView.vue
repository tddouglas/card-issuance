<template>
	<div class="flex justify-center items-center flex-col">
		<new-order-event-details></new-order-event-details>
	</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import NewOrderEventDetails from '@/components/newOrder/newOrderEventDetails.vue'

export default defineComponent({
	name: 'NewOrderView',
	components: { NewOrderEventDetails },
})
</script>

<template>
	<div>
		<div v-if="userOrders.length > 0">
			<existing-orders-grid></existing-orders-grid>
		</div>
		<div v-else>
			<h1>No Existing Orders</h1>
		</div>
	</div>
</template>

<script lang="ts">
import {defineComponent} from "vue"
import ExistingOrdersGrid from "@/components/ExistingOrdersGrid.vue";
import type CardOrderItem from "@/types/cardOrderItem";

export default defineComponent({
	name: "ExistingOrderView",
	components: {ExistingOrdersGrid},
	methods: {},
	mounted() {
		this.userOrders = [{
			numberOfCards: 2,
			program: "Recruiting"
		}]
	},
	data() {
		return {
			userOrders: [] as CardOrderItem[]
		}
	}
})
</script>



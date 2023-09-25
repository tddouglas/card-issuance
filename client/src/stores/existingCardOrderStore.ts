import { defineStore } from 'pinia'
import { getBackend } from '@/helpers/fetchUtil'
import type ExistingOrders from '@/types/existingOrders'

export const existingCardOrderStore = defineStore('existingCardOrder', {
	state: () => {
		return {
			exisingCardOrders: [] as Array<Object>,
			selectedOrder: {},
		}
	},
	getters: {
		formatExistingCardOrders(): Array<object> {
			// Matching Headers - ['Card Order ID', 'Number of Cards', 'Status', 'Event Type']
			const res = []
			for (const order of this.exisingCardOrders) {
				res.push([
					order.id,
					order.number_of_cards,
					order.shipping_status,
					order.approved_usecase_id,
				])
			}
			console.log("Formatting existing orders", res)
			return res
		},
	},
	actions: {
		async setAllCardOrders(): Promise<void> {
			this.exisingCardOrders = await getBackend('orders/')
		},
		async setSelectedOrder(orderId: string): Promise<void> {
			this.selectedOrder = await getBackend(`orders/${orderId}`)
		},
		async getExistingCardOrder(order_id: string): Promise<Array<Object>> {
			return await getBackend(`orders/{${order_id}`)
		},
	},
	persist: true,
})

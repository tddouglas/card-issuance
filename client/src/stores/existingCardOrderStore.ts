import { defineStore } from 'pinia'
import { getBackend } from '@/helpers/fetchUtil'
import {
	ExistingOrdersDisplay,
	ExistingOrdersBase,
	ExistingOrderDetailsCard,
} from '@/types/existingOrders'
import { eventTypeToEnum } from '@/types/eventType'
import { cardOrderStatusToEnum } from '@/types/cardOrderStatus'

export const existingCardOrderStore = defineStore('existingCardOrder', {
	state: () => {
		return {
			exisingCardOrders: [] as Array<ExistingOrdersBase>,
			selectedOrderCards: [] as Array<ExistingOrderDetailsCard>,
		}
	},
	getters: {
		formatExistingCardOrders(): Array<any> {
			// Matching Headers - ['Card Order ID', 'Number of Cards', 'Status', 'Event Type']
			const res = []
			for (const order of this.exisingCardOrders) {
				const orderDisplayObj = new ExistingOrdersDisplay(
					order.id,
					order.numberOfCards,
					cardOrderStatusToEnum(order.shippingStatus),
					eventTypeToEnum(order.approvedUseCaseId),
					order.cardOrderId
				)
				res.push(orderDisplayObj.toStringArray())
			}
			return res
		},
		isSelectedOrderEmpty(): boolean {
			return Object.keys(this.selectedOrderCards).length === 0
		},
		formatSelectedOrderCards(): Array<any> {
			const res = []
			for (const order of this.selectedOrderCards) {
				res.push(order.toStringArray())
			}
			return res
		}
	},
	actions: {
		async setExistingCardOrders(): Promise<void> {
			const res = await getBackend('orders/')
			const ret = [] as Array<ExistingOrdersBase>
			for (const order of res) {
				ret.push(
					new ExistingOrdersBase(
						order.id,
						order.requesting_user,
						order.number_of_cards,
						order.approved_usecase_id,
						order.event_start_date,
						order.event_end_date,
						order.card_shipping_address,
						order.logo_id,
						order.card_order_id,
						order.shipping_status
					)
				)
			}
			this.exisingCardOrders = ret
		},
		async setSelectedOrderCards(orderId: string): Promise<void> {
			const res = await getBackend(`orders/${orderId}/cards`)
			const ret = [] as Array<ExistingOrderDetailsCard>
			for (const card of res) {
				ret.push(
					new ExistingOrderDetailsCard(
						card.id,
						card.payment_instrument_id,
						card.cardholder_name,
						card.status,
						card.order_id
					)
				)
			}
			this.selectedOrderCards = ret
		},
	},
	persist: false,
})

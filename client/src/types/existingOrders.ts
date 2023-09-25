import type CardOrderStatus from '@/types/cardOrderStatus'
import type EventType from '@/types/eventType'

export default interface ExistingOrders {
	id: number,
	numberOfCards: number,
	cardOrderStatus: CardOrderStatus
	eventType: EventType
}

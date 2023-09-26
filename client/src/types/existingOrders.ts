import type { CardOrderStatus } from '@/types/cardOrderStatus'
import type { EventType } from '@/types/eventType'
import { CardStatus, cardStatusToEnum } from '@/types/cardStatus'

export class ExistingOrdersDisplay {
	id: number
	numberOfCards: number
	cardOrderStatus: CardOrderStatus
	eventType: EventType
	cardOrderId?: string

	constructor(
		id: number,
		numberOfCards: number,
		cardOrderStatus: CardOrderStatus,
		eventType: EventType,
		cardOrderId?: string
	) {
		this.id = id
		this.numberOfCards = numberOfCards
		this.cardOrderStatus = cardOrderStatus
		this.eventType = eventType
		this.cardOrderId = cardOrderId
	}

	toStringArray(): Array<any> {
		const cardOrderId = this.cardOrderId
			? this.cardOrderId
			: 'ID not received yet'
		return [
			{
				id: this.id.toString(),
				cardOrderId: cardOrderId,
			},
			this.numberOfCards.toString(),
			this.cardOrderStatus,
			this.eventType,
		]
	}
}

export class ExistingOrdersBase {
	id: number
	cardOrderId?: string
	shippingStatus?: string
	requestingUser: string
	numberOfCards: number
	approvedUseCaseId: number
	eventStartDate: string
	eventEndDate: string
	cardShippingAddress: string
	logoId: number

	constructor(
		id: number,
		requestingUser: string,
		numberOfCards: number,
		approvedUseCaseId: number,
		eventStartDate: string,
		eventEndDate: string,
		cardShippingAddress: string,
		logoId: number,
		cardOrderId?: string,
		shippingStatus?: string
	) {
		this.id = id
		this.requestingUser = requestingUser
		this.numberOfCards = numberOfCards
		this.approvedUseCaseId = approvedUseCaseId
		this.eventStartDate = eventStartDate
		this.eventEndDate = eventEndDate
		this.cardShippingAddress = cardShippingAddress
		this.logoId = logoId
		this.cardOrderId = cardOrderId
		this.shippingStatus = shippingStatus
	}
}

export class ExistingOrderDetailsCard {
	id: number
	paymentInstrumentId: string
	cardholderName: string
	status: CardStatus
	orderId: number

	constructor(
		id: number,
		paymentInstrumentId: string,
		cardholderName: string,
		status: string,
		orderId: number
	) {
		this.id = id
		this.paymentInstrumentId = paymentInstrumentId
		this.cardholderName = cardholderName
		this.status = cardStatusToEnum(status)
		this.orderId = orderId
	}

	toStringArray(): Array<string> {
		return [this.status, this.paymentInstrumentId, this.cardholderName]
	}
}

enum CardOrderStatus {
	PENDING = 'Pending',
	CREATED = 'Created',
	SHIPPED = 'Shipped',
	CLOSED = 'Closed',
}

function cardOrderStatusToEnum(status: string | undefined): CardOrderStatus {
	let cardOrderStatus
	switch (status) {
		case 'Created':
			cardOrderStatus = CardOrderStatus.CREATED
			break
		case 'Shipped':
			cardOrderStatus = CardOrderStatus.SHIPPED
			break
		case 'Closed':
			cardOrderStatus = CardOrderStatus.CLOSED
			break
		default:
			cardOrderStatus = CardOrderStatus.PENDING
	}
	return cardOrderStatus
}

export { CardOrderStatus, cardOrderStatusToEnum }

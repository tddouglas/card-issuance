enum CardStatus {
	ACTIVE = 'Active',
	INACTIVE = 'Inactive',
	REQUESTED = 'Requested',
	CLOSED = 'Closed',
}

function cardStatusToEnum(status: string | undefined): CardStatus {
	let cardStatus
	switch (status) {
		case 'active':
			cardStatus = CardStatus.ACTIVE
			break
		case 'inactive':
			cardStatus = CardStatus.INACTIVE
			break
		case 'requested':
			cardStatus = CardStatus.REQUESTED
			break
		case 'closed':
			cardStatus = CardStatus.CLOSED
			break
		default:
			throw new Error("Card Status not in Enum")
	}
	return cardStatus
}

export { CardStatus, cardStatusToEnum }

enum EventType {
	RECRUITING = 'Recruiting',
	INTERNAL = 'Internal',
}

function eventTypeToEnum(eventId: string | number): EventType {
	let eventType
	switch (eventId) {
		case 'Recruiting':
		case 1:
			eventType = EventType.RECRUITING
			break
		case 'Internal':
		case 2:
			eventType = EventType.INTERNAL
			break
		default:
			throw new Error(`No corresponding Event Strings found for ${eventId}`)
	}
	return eventType
}

export { EventType, eventTypeToEnum }

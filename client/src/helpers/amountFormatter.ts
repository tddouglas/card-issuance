function formatAmount(minorUnits: number, currency: string) {
	let currencySymbol = ''
	if (currency == 'EUR') {
		currencySymbol = '€'
	} else if (currency == 'USD') {
		currencySymbol = '$'
	}

	const minorUnitsString = minorUnits.toString()
	if (!(minorUnits < 100)) {
		const decimalAmount =
			minorUnitsString.slice(0, minorUnitsString.length - 2) +
			'.' +
			minorUnitsString.slice(minorUnitsString.length - 2)
		return currencySymbol + decimalAmount
	} else {
		throw Error('Too small number provided in minorUnits')
	}
}

export { formatAmount }

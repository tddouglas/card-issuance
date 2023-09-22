import { defineStore } from 'pinia'

export const newCardOrderStore = defineStore('newCardOrder', {
	state: () => {
		return {
			selectedCountry: '',
			selectedOrderType: '',
			numberOfCards: 0,
			eventStartDate: '',
			eventEndDate: '',
			selectedImage: '',
			selectedAddress: '',
		}
	},
	getters: {
		isCountrySet(): boolean {
			return this.selectedCountry != ''
		},
		isMainOrderSet(): boolean {
			return this.selectedCountry != '' && this.selectedOrderType != ''
		},
		isOrderEventDetailsValid(): boolean {
			return (
				this.numberOfCards > 0 &&
				this.eventStartDate.length > 0 &&
				this.eventEndDate.length > 0 &&
				this.selectedImage.length > 0 &&
				this.selectedAddress.length > 0
			)
		},
	},
	actions: {
		resetMainOrder() {
			this.selectedCountry = ''
			this.selectedOrderType = ''
		},
		resetOrderDetails() {
			this.numberOfCards = 0
			this.eventStartDate = ''
			this.eventEndDate = ''
			this.selectedImage = ''
		},
	},
	persist: true,
})

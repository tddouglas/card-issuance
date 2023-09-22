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
		}
	},
	getters: {
		isMainOrderSet(): boolean {
			const x = this.selectedCountry != '' && this.selectedOrderType != ''
			return x
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

import { defineStore } from 'pinia'

export const newCardOrderStore = defineStore('newCardOrder', {
	state: () => {
		return {
			selectedCountry: '',
			selectedOrderType: '',
			numberOfCards: 0,
			eventStartDate: '',
			eventEndDate: '',
			selectedAddress: '',
			selectedImage: '',
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
		getNewCardOrderObject(): object {
			return {
				'requesting_user': '',
				'number_of_cards': this.numberOfCards,
				'approved_usecase_id': 0, // Store approvedUsecaseId in store
				'event_start_date': this.eventStartDate,
				'event_end_date': this.eventEndDate,
				'card_shipping_address': this.selectedAddress,
				'logo_id': 0, //TODO: set logo id dynamically
			}
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

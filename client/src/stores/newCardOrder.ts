import {defineStore} from 'pinia'

export const newCardOrderStore = defineStore('newCardOrder', {
    state: () => {
        return {
            selectedCountry: "",
            selectedOrderType: "",
            numberOfCards: 0,
            eventStartDate: "",
            entEndDate: "",
            selectedImage: ""
        }
    }
})

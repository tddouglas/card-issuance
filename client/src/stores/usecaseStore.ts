import { defineStore } from 'pinia'
import { getBackend } from '@/helpers/fetchUtil'
import { newCardOrderStore } from '@/stores/newCardOrder'

export const usecaseStore = defineStore('usecase', {
	state: () => {
		return {
			approvedUsecases: [],
		}
	},
	actions: {
		async getApprovedUsecases(): Promise<void> {
			const res = await getBackend('usecases')
			if (res) {
				this.approvedUsecases = res
			}
		},
		getUniqueCountries(): Array<string> {
			const uniqueList: string[] = []
			for (const usecase of this.approvedUsecases) {
				if ('allowed_countries' in usecase) {
					if (!uniqueList.includes(usecase['allowed_countries']))
						uniqueList.push(usecase['allowed_countries'])
				}
			}
			return uniqueList
		},
		getUniqueEventTypes(): Array<string> {
			const uniqueList: string[] = []
			for (const usecase of this.approvedUsecases) {
				const selectedCountry = newCardOrderStore().selectedCountry
				if (
					'event_type' in usecase &&
					usecase['allowed_countries'] == selectedCountry
				) {
					if (!uniqueList.includes(usecase['event_type']))
						uniqueList.push(usecase['event_type'])
				}
			}
			return uniqueList
		},
	},
	persist: false,
})

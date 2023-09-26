<template>
	<the-dropdown
		:dropdown-options="cardOrderImageOptions"
		class="mb-8"
		@set="setImage">
		<template #dropdown-text>Select Image to use on card</template>
	</the-dropdown>
	<new-order-image-preview
		v-if="imgPreviewPath"
		class="w-96"
		:image-path="imgPreviewPath"></new-order-image-preview>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import NewOrderImagePreview from '@/components/newOrder/newOrderImagePreview.vue'
import TheDropdown from '@/components/TheDropdown.vue'
import AdyenWalletImg from '@/assets/images/card_art/adyen-wallet.png'
import FashionWeekImg from '@/assets/images/card_art/fashion-week-23.png'
import { mapStores } from 'pinia'
import { newCardOrderStore } from '@/stores/newCardOrder'

export default defineComponent({
	name: 'NewOrderCardArtSelection',
	components: { TheDropdown, NewOrderImagePreview },
	computed: {
		...mapStores(newCardOrderStore),
		// Return img path if selectedImage is set in store. Otherwise return Falsey value
		imgPreviewPath(): string {
			const img = this.newCardOrderStore.selectedImage
			if (img == 'Adyen Fast Card') {
				return this.adyenWalletImg
			} else if (img == 'Fashion Week') {
				return this.fashionWeekImg
			}
			return ''
		},
	},
	methods: {
		setImage(image: string) {
			this.newCardOrderStore.selectedImage = image
		},
	},
	data() {
		return {
			adyenWalletImg: AdyenWalletImg,
			fashionWeekImg: FashionWeekImg,
			cardOrderImageOptions: ['Adyen Fast Card', 'Fashion Week'],
		}
	},
})
</script>
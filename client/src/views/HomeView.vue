<template>
	<div class="flex flex-wrap justify-center">
		<the-tile title="Existing Card Order" path="existingCardOrder" :img-logo="multipleCardsImg" class="md:mr-20">
			<template #tile-description>
				View existing card orders.
			</template>
		</the-tile>
		<the-tile title="New Card Order" path="newCardOrder" :img-logo="cardEditImg">
			<template #tile-description>
				Place a new card order from a pre-approved program.
			</template>
		</the-tile>
	</div>
</template>

<script lang="ts">
import {defineComponent} from "vue"
import TheTile from "@/components/TheTile.vue";
import CardEditImg from "@/assets/images/card_edit.svg"
import MultipleCardsImg from "@/assets/images/multiple_cards.svg"

export default defineComponent({
	name: "HomeView",
	components: {TheTile},
	methods: {},
	data() {
		return {
			cardEditImg: CardEditImg,
			multipleCardsImg: MultipleCardsImg
		}
	}
})
</script>



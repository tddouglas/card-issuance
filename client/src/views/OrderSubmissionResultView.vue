<template>
	<div v-if='$route.query.success' class="">
		<h1 class="font-bold text-3xl mb-4">Order Successfully Submitted</h1>
		<p>Thank you for placing a card order.</p>
		<p>
			It will take some time for the cards to be manufactured and shipped.
			You can stay up to date on the latest status of your order by
			visiting the
			<router-link to="/existingCardOrder" class='underline'>Existing Orders tab</router-link>
		</p>
	</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
	name: 'OrderSubmissionResultsView',
	components: {},
	data() {
		return {
		}
	},
})
</script>

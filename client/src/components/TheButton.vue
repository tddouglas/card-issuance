<template>
	<button
		:ref="reference"
		:disabled='loading'
		class="bg-adyen-light rounded-lg text-adyen-light-text hover:bg-adyen-grey px-4 py-2 font-semibold">
		<the-spinner :loading='loading'></the-spinner>
		<slot name="button-text"></slot>
	</button>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import TheSpinner from '@/components/TheSpinner.vue'

export default defineComponent({
	name: 'TheButton',
	components: { TheSpinner },
	props: {
		reference: {
			required: false,
			type: String,
		},
		focus: {
			required: false,
			type: Boolean,
		},
		loading: {
			required: false,
			type: Boolean,
		},
	},
	mounted() {
		if (this.focus) {
			// @ts-ignore
			this.$refs[this.reference].focus()
		}
	},
	data() {
		return {
		}
	},
})
</script>

<template>
	<div>
		<!-- TODO: Move input label like here - https://www.adyen.com/signup -->
		<!-- TODO: Add validation to inputs -->
		<input
			max="1000"
			min="1"
			type="number"
			inputmode="numeric"
			pattern="\d*"
			:placeholder="labelText"
			class="rounded w-full h-full text-adyen-light-text px-2 focus-visible:outline-4 focus-visible:outline-green focus-visible:outline"
			v-model.lazy.number="inputNumber"
			@change="setSelected" />
	</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
	name: 'TheInputNumber',
	emits: ['set'],
	props: {
		labelText: {
			required: true,
			type: String,
		},
	},
	methods: {
		setSelected() {
			this.$emit('set', this.inputNumber)
		},
	},
	data() {
		return {
			inputNumber: null as Number | null,
		}
	},
})
</script>

<template>
	<div>
		<input :min="currentDate" type="date" class="rounded w-full h-full text-adyen-light-text px-2 focus-visible:outline-4 focus-visible:outline-green focus-visible:outline" @input="setSelected">
	</div>
</template>

<script lang="ts">
import {defineComponent} from "vue"

export default defineComponent({
	name: "TheInputDate",
	emits: ['set'],
	computed: {
		currentDate(): string {
			const date = new Date()
			return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`
		}
	},
	methods: {
		setSelected(input: string) {
			this.$emit("set", input)
		}
	},
	data() {
		return {}
	}
})
</script>



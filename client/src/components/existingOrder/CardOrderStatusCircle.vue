<template>
	<div
		class="w-3 h-3 rounded-full inline-block mr-1"
		:class="cardStatusBackground"></div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
	name: 'CardOrderStatusCircle',
	props: {
		radius: {
			required: true,
			type: String,
		},
		status: {
			required: true,
			type: String,
		},
	},
	computed: {
		cardStatusBackground(): Object {
			return {
				'bg-active': this.status == 'Active',
				'bg-inactive': this.status == 'Inactive',
			}
		},
	},
	data() {
		return {}
	},
})
</script>

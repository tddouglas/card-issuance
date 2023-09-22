<template>
	<div class="w-3 h-3 rounded-full bg-adyen-light inline-block mr-1"></div>
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
	},
	data() {
		return {}
	},
})
</script>

<template>
	<div>
		<img :src='imagePath' alt='Card Art Image' class='rounded-xl'/>
	</div>
</template>

<script lang='ts'>
import { defineComponent } from 'vue'

export default defineComponent({
	name: "NewOrderImagePreview",
	props: {
		imagePath: {
			required: true,
			type: String
		}
	}
})
</script>
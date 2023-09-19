<template>
	<router-link class="hover:shadow-tileShadow w-72 h-48 rounded-md border p-8 mb-8 cursor-pointer" :to="path">
		<div class="m-0">
			<p class="text-center">
				<img alt="Tile Img" class="w-12 mx-auto mb-2" :src="imgLogo">
				<span class="text-[18px]/[21px] mb-4">
					<strong>{{ title }}</strong>
				</span>
				<br>
				<slot name="tile-description"/>
			</p>
		</div>
	</router-link>
</template>

<script lang="ts">
import {defineComponent} from "vue"

export default defineComponent({
	name: "TheTile",
	props: {
		title: {
			required: true,
			type: String
		},
		path: {
			required: true,
			type: String
		},
		imgLogo: {
			required: true,
			type: String
		}
	},
	data() {
		return {}
	}
})
</script>



<template>
	<nav class="mt-8 grid h-10 grid-cols-3 items-center">
		<div class="">
			<img :src="adyenLogo" alt="Website Logo" class="w-36"/>
		</div>
		<router-link to="/">
			<div class="text-center text-2xl font-bold">Adyen Card Issuance</div>
		</router-link>
		<div class="text-right">
			Welcome <em>tyler@adyen.com</em>
		</div>
	</nav>
</template>
<script lang="ts">
import {defineComponent} from "vue"
import {RouterLink} from "vue-router"
import adyenLogo from "@/assets/images/adyen_logo_large.svg"

export default defineComponent({
	name: "TheNavbar",
	components: {RouterLink},
	data() {
		return {
			adyenLogo: adyenLogo,
		}
	}
})
</script>

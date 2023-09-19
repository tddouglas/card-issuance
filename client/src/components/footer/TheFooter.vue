<template>
	<footer class="relative bottom-0 pb-4 pt-6">
		<div class="grid grid-cols-3">
			<div class="text-secondary self-center justify-self-start text-xs">
				Copyright © Adyen. All rights reserved.
			</div>
			<div class="self-center justify-self-center">
				<RouterLink to="/">
					<img
						:src="adyenLogo"
						alt="TylerDouglas.co Logo"
						class="w-8"
					/>
				</RouterLink>
			</div>
			<div class="self-center justify-self-end">
			</div>
		</div>
	</footer>
</template>

<script lang="ts">
import {defineComponent} from "vue"
import {RouterLink} from "vue-router"
import adyenLogo from "@/assets/images/adyen_logo.svg"

export default defineComponent({
	name: "TheFooter",
	components: {RouterLink},
	data() {
		return {
			adyenLogo: adyenLogo,
		}
	}
})
</script>

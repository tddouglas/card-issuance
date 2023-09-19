<template>
	<div
		class="container mx-auto max-w-screen-lg flex-auto px-2 font-body text-adyen-dark-text md:px-6"
	>
		<the-navbar/>
		<main class="flex min-h-[50vh] flex-col items-center mt-24">
			<div class="mb-10 w-10/12 md:w-3/4">
				<router-view/>
			</div>
		</main>
<!--		<the-footer/>-->
	</div>
</template>

<script lang="ts">
import { defineComponent } from "vue"
import TheNavbar from "@/components/navbar/TheNavbar.vue";
import TheFooter from "@/components/footer/TheFooter.vue";

import {RouterLink, RouterView} from 'vue-router'

export default defineComponent({
	components: {TheNavbar, TheFooter, RouterView}
})
</script>


<style scoped>
</style>

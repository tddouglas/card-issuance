<template>
	<div>
		<the-grid :rows="tableRows" :headers="tableHeaders"></the-grid>
	</div>
</template>

<script lang="ts">
import {defineComponent, type PropType} from "vue"
import TheGrid from "@/components/TheGrid.vue";

export default defineComponent({
	name: "ExistingOrderGrid",
	components: {TheGrid},
	methods: {},
	data() {
		return {
			tableHeaders: ["Card Status", "Cardholder Name", "Event Start", "Event End"],
			tableRows: [["Shipped", "NA Recruiting0", "05-10-2023", "05-11-2023"],
				["Shipped", "NA Recruiting1", "05-10-2023", "05-11-2023"],
				["Shipped", "NA Recruiting2", "05-10-2023", "05-11-2023"],
				["Shipped", "NA Recruiting3", "05-10-2023", "05-11-2023"]]
		}
	}
})
</script>



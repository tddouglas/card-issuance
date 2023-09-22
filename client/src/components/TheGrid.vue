<template>
	<table class="table-auto">
		<thead>
		<tr class="border-b">
			<th v-for="header in headers" :key="header" class="pb-2 text-left pr-8">{{ header }}</th>
		</tr>
		</thead>
		<tbody>
		<tr v-for="(row, index) in rows" :key="index">
			<td v-for="cell in row" :key="cell" class="pt-2 min-w-[150px]">{{ cell }}</td>
		</tr>
		</tbody>
	</table>
</template>

<script lang="ts">
import {defineComponent} from "vue"

export default defineComponent({
	name: "TheGrid",
	props: {
		headers: {
			required: true,
			type: Array<string>
		},
		rows: {
			required: true,
			type: Array<Array<string>>
		}
	},
	data() {
		return {}
	}
})
</script>



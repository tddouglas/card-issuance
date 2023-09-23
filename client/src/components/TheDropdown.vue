<template>
	<div>
		<div
			@click="toggleDropdown"
			class="w-96 h-12 rounded bg-adyen-light text-adyen-light-text px-2 border-2 border-adyen-white cursor-pointer flex hover:border-adyen-grey mb-2"
			:class="{ 'border-green hover:border-green': showOptions }">
			<span
				v-if="!selected"
				class="opacity-60 text-sm font-dropdown leading-[3rem]"
				><slot name="dropdown-text"></slot
			></span>
			<span v-else class="text-sm font-dropdown leading-[3rem]">{{
				selected
			}}</span>
			<img
				:src="arrowImg"
				alt="dropdown arrow"
				class="inline-block ml-auto mr-2 w-4 transition-all ease-in-out duration-200"
				:class="{ 'rotate-180': showOptions }" />
		</div>
		<ul
			class="text-sm bg-adyen-light rounded text-adyen-light-text"
			:class="{ hidden: !showOptions }"
			aria-labelledby="dropdownDefaultButton">
			<li
				v-for="option in dropdownOptions"
				:key="option"
				class="rounded p-2 cursor-pointer hover:bg-adyen-grey hover:underline"
				@click="setSelected(option)">
				<span>{{ option }}</span>
			</li>
		</ul>
	</div>
</template>

<script lang="ts">
import {defineComponent} from "vue";
import arrowImg from "@/assets/images/arrow.svg";

export default defineComponent({
	name: "TheDropdown",
	emits: ['set'],
	props: {
		dropdownOptions: {
			required: true,
			type: Array<string>,
		}
	},
	methods: {
		toggleDropdown() {
			this.showOptions = !this.showOptions;
		},
		setSelected(option: string) {
			this.selected = option
			this.$emit("set", this.selected)
			this.showOptions = false
		}
	},
	beforeUpdate() {
		if (!this.dropdownOptions.includes(this.selected)) {
			this.selected = ""
		}
	},
	data() {
		return {
			arrowImg: arrowImg,
			showOptions: false,
			selected: ""
		};
	},
});
</script>

<style scoped>
.rotated {
	@apply;
}

.transition {
	transition: transform 0.5s ease-in-out;
}
</style>
<script setup lang="ts">
import { computed } from "vue";
import { useServerStore } from "../store/server";
import { useRoute } from "vue-router";

const route = useRoute();
const server = useServerStore();
server.getGrafanaPanels();

const grafanaPanels = computed(() => server.grafanaPanels);
const isGrafanaPanelsFetched = computed(() => server.isGrafanaPanelsFetched);
</script>

<template>
  <div>
    <iframe
      v-if="isGrafanaPanelsFetched"
      :src="grafanaPanels![0].url"
      width="1100"
      height="200"
      frameborder="0"
    ></iframe>
  </div>
</template>

<style scoped></style>

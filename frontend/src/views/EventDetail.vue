<script setup lang="ts">
import { computed } from "vue";
import { useServerStore } from "../store/server";
import { useRoute } from "vue-router";

const route = useRoute();
const query = <{ server: string }>route.query;
const server = useServerStore();

server.getGrafanaPanels(query.server);

const grafanaPanels = computed(() => server.grafanaPanels);
const isGrafanaPanelsFetched = computed(() => server.isGrafanaPanelsFetched);
</script>

<template>
  <div>
    <iframe
      v-if="isGrafanaPanelsFetched"
      v-for="grafanaPanel in grafanaPanels"
      :key="grafanaPanel.url"
      :src="grafanaPanel.url"
      width="1100"
      height="200"
      frameborder="0"
    ></iframe>
  </div>
</template>

<style scoped></style>

<script setup lang="ts">
import { computed } from "vue";
import { useServerStore } from "../store/server";
import { useRoute } from "vue-router";

const route = useRoute();
const query = route.query as { server: string };
const server = useServerStore();

server.getGrafanaPanels(query.server);

const grafanaPanels = computed(() => server.grafanaPanels);
const isGrafanaPanelsFetched = computed(() => server.isGrafanaPanelsFetched);
const eventError = computed(() => server.eventError);
</script>

<template>
  <div v-if="!eventError">
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
  <div v-else>{{ eventError }}</div>
</template>

<style scoped></style>

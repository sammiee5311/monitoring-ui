<script setup lang="ts">
import { useServerStore } from "../store/server";
import { computed } from "@vue/reactivity";

const server = useServerStore();
server.getSentryEvents();

const sentryEventList = computed(() => server.sentryEvents);
const isEventsFetched = computed(() => server.isEventsFetched);
</script>

<template>
  <div class="d-flex justify-content-center" v-if="!isEventsFetched">
    <div class="spinner-border" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
  </div>
  <div class="list-group" v-for="event of sentryEventList" :key="event.eventID">
    <a
      :href="`http://localhost:9000/sentry/fast-api/events/${event.eventID}/`"
      class="list-group-item list-group-item-action"
    >
      {{ event.title }}
    </a>
  </div>
</template>

<style scoped></style>

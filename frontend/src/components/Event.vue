<script setup lang="ts">
import { useServerStore } from "../store/server";
import { computed } from "@vue/reactivity";
import router from "../routers";

const server = useServerStore();
server.getSentryEvents();

const sentryEventList = computed(() => server.sentryEvents);
const isEventsFetched = computed(() => server.isEventsFetched);

const goToEventDetail = (eventId: string, eventServer: string) => {
  router.push({ path: `/list/event/${eventId}`, query: { server: eventServer } });
};
</script>

<template>
  <div class="d-flex justify-content-center" v-if="!isEventsFetched">
    <div class="spinner-border" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
  </div>
  <div class="list-group" v-for="event of sentryEventList" :key="event.eventID">
    <div
      :href="`http://localhost:9000/sentry/fast-api/events/${event.eventID}/`"
      class="list-group-item list-group-item-action"
      @click="goToEventDetail(event.eventID, 'server')"
    >
      {{ event.title }} | {{ event.tags.find((tag) => tag.key === "server_name")?.value }} |
      {{ event.tags.find((tag) => tag.key === "url")?.value }}
    </div>
  </div>
</template>

<style scoped></style>

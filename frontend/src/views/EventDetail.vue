<script setup lang="ts">
import { useServerStore } from "../store/server";
import { useRoute } from "vue-router";

const route = useRoute();
const server = useServerStore();

const eventId = route.params.eventId;
</script>

<template>
  <div>
    <iframe
      src="http://localhost:3030/d-solo/OnfS5Lqnz/init?orgId=1&from=1656486968140&to=1656508568140&panelId=2"
      width="1100"
      height="200"
      frameborder="0"
    ></iframe>
  </div>
</template>

<style scoped></style>

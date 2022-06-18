<script setup lang="ts">
import { useServerStore } from "../store/server";
import { computed } from "@vue/reactivity";

const server = useServerStore();
const message = computed(() => server.message);

server.initConnectBackend();
</script>

<template>
  <div>{{ message }}</div>
</template>

<style scoped></style>

<script setup lang="ts">
import { useServerStore } from "../store/server";
import { computed } from "@vue/reactivity";

const server = useServerStore();
server.getSentryIssues();

const sentryIssueList = computed(() => server.sentryIssues);
const isIssuesFetched = computed(() => server.isIssuesFetched);
</script>

<template>
  <div class="d-flex justify-content-center" v-if="!isIssuesFetched">
    <div class="spinner-border" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
  </div>
  <div class="list-group" v-for="issue of sentryIssueList" :key="issue.id">
    <a :href="issue.permalink" class="list-group-item list-group-item-action">
      {{ issue.title }}
    </a>
  </div>
</template>

<style scoped></style>

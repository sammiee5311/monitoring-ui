<script setup lang="ts">
import Issue from "../components/Issue.vue";
import Event from "../components/Event.vue";

import { ref } from "@vue/reactivity";

let currentTab = ref("event");

const onButtonClicked = (event: Event) => {
  currentTab.value = (event.target as HTMLBaseElement).id;
};
</script>

<template>
  <ul class="nav nav-tabs">
    <li class="nav-item">
      <a class="nav-link" id="event" href="#" @click="onButtonClicked">Event</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" id="issue" href="#" @click="onButtonClicked">Issue</a>
    </li>
  </ul>

  <div v-if="currentTab === 'event'"><Event /></div>

  <div v-if="currentTab === 'issue'"><Issue /></div>
</template>

<style scoped></style>

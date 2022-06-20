<script setup lang="ts">
import { RouterView } from "vue-router";
import Header from "./components/ui/Header.vue";
import Footer from "./components/ui/Footer.vue";
</script>

<template>
  <div>
    <Header />
    <RouterView />
    <Footer />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>

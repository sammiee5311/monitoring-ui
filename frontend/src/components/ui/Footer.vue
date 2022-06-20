<script setup lang="ts">
const year = new Date().getFullYear();
</script>

<template>
  <footer
    class="text-center p-4"
    style="background-color: rgba(0, 0, 0, 0.05); width: 100%; position: absolute; bottom: 0; left: 0"
  >
    {{ year }} Copyright:
    <a class="text-reset fw-bold">sammiee5311</a>
  </footer>
</template>

<style scoped></style>

/// <reference types="vitest" />
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
  server: {
    proxy: {
      "/api/v0": "https://localhost",
    },
  },
  test: {
    environment: "jsdom",
    globals: true,
  },
  plugins: [vue()],
});

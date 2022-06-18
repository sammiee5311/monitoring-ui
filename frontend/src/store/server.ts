import { defineStore } from "pinia";
import axios from "axios";

import { ServerState, ResponseData } from "../types/store";

const getServerState = () => {
  return {
    message: "",
  };
};

export const useServerStore = defineStore("server", {
  state: (): ServerState => getServerState(),
  getters: {},
  actions: {
    async initConnectBackend() {
      try {
        const response = await axios.get("/api/v0/temp/");
        const data: ResponseData = response.data;

        this.message = data.message;
      } catch (err) {
        this.message = `Frontend cannot connect to Backend (${err})`;
      }
    },
  },
});

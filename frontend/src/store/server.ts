import { defineStore } from "pinia";
import axios from "axios";

import { ServerState, ResponseData, SentryEvent, SentryIssue } from "../types/store";

const getServerState = () => {
  return {
    message: "",
    authToken: "3ac9f50f3eec42cba9b8715d38531e3e56eaf6ae32ee41769c5e13947699af88",
    isEventsFetched: false,
    isIssuesFetched: false,
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

    async getSentryEvents() {
      try {
        const response = await axios.get("/api/0/projects/sentry/fast-api/events/", {
          headers: {
            Authorization: `Bearer ${this.authToken}`,
          },
        });
        const data: SentryEvent[] = response.data;

        this.sentryEvents = data;
      } catch (err) {
      } finally {
        this.isEventsFetched = true;
      }
    },

    async getSentryIssues() {
      try {
        const response = await axios.get("/api/0/projects/sentry/fast-api/issues/", {
          headers: {
            Authorization: `Bearer ${this.authToken}`,
          },
        });
        const data: SentryIssue[] = response.data;

        this.sentryIssues = data;
      } catch (err) {
      } finally {
        this.isIssuesFetched = true;
      }
    },
  },
});

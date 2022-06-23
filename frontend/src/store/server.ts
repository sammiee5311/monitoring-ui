import { defineStore } from "pinia";
import axios from "axios";
import { AxiosResponse } from "axios";

import { ServerState, ResponseData, SentryEvent, SentryIssue } from "../types/store";

const TIMEOUT_SECOND = 1000 * 60;

const sleep = (ms: number): Promise<string> => {
  return new Promise((resolve) => setTimeout(resolve, ms, "Timeout occured during api call."));
};

const getServerState = () => {
  return {
    message: "",
    authToken: import.meta.env.VITE_SENTRY_AUTH_TOKEN as string,
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
        const response = await Promise.race<string | AxiosResponse<ResponseData, any>>([
          axios.get("/api/v0/temp/"),
          sleep(TIMEOUT_SECOND),
        ]);

        if (typeof response === "string") {
          throw new Error(response);
        }

        const data = response.data;

        this.message = data.message;
      } catch (err) {
        this.message = `Frontend cannot connect to Backend (${err})`;
      }
    },

    async getSentryEvents() {
      try {
        const response = await Promise.race<string | AxiosResponse<SentryEvent[], any>>([
          axios.get("/api/0/projects/sentry/fast-api/events/", {
            headers: {
              Authorization: `Bearer ${this.authToken}`,
            },
          }),
          sleep(TIMEOUT_SECOND),
        ]);

        if (typeof response === "string") {
          throw new Error(response);
        }

        const data = response.data;

        this.sentryEvents = data;
      } catch (err) {
      } finally {
        this.isEventsFetched = true;
      }
    },

    async getSentryIssues() {
      try {
        const response = await Promise.race<string | AxiosResponse<SentryIssue[], any>>([
          axios.get("/api/0/projects/sentry/fast-api/issues/", {
            headers: {
              Authorization: `Bearer ${this.authToken}`,
            },
          }),
          sleep(TIMEOUT_SECOND),
        ]);

        if (typeof response === "string") {
          throw new Error(response);
        }

        const data = response.data;

        this.sentryIssues = data;
      } catch (err) {
      } finally {
        this.isIssuesFetched = true;
      }
    },
  },
});

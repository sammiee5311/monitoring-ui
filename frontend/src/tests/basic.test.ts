import { mount } from "@vue/test-utils";
import { setActivePinia, createPinia } from "pinia";
import { expect, test } from "vitest";
import { useServerStore } from "../store/server";

import IDontKnowName from "../components/IDontKnowName.vue";

beforeEach(() => {
  setActivePinia(createPinia());
});

test("displays message", () => {
  const server = useServerStore();

  server.initConnectBackend();
  server.$patch({ message: "Hello World" });

  const wrapper = mount(IDontKnowName);

  expect(wrapper.text()).toBe("Hello World");
});

import { mount } from "@vue/test-utils";
import { expect, test } from "vitest";
import IDontKnowName from "../components/IDontKnowName.vue";

test("displays message", () => {
  const wrapper = mount(IDontKnowName);

  expect(wrapper.text()).toContain("Hello World");
});

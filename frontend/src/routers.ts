import { createRouter, createWebHistory } from "vue-router";

import Home from "./views/Home.vue";
import List from "./views/List.vue";
import Demo from "./views/Demo.vue";
import EventDetail from "./views/EventDetail.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home,
    },
    {
      path: "/list",
      name: "List",
      component: List,
    },
    {
      path: "/list/event/:eventId",
      name: "EventDetail",
      component: EventDetail,
    },
    {
      path: "/demo",
      name: "Demo",
      component: Demo,
    },
  ],
});

export default router;

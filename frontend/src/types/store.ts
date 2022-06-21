export type ServerState = {
  message: string;
  authToken: string;
  sentryEvents?: SentryEvent[];
  sentryIssues?: SentryIssue[];
  isEventsFetched: boolean;
  isIssuesFetched: boolean;
};

export type ResponseData = {
  message: string;
};

type SentryEventTag = {
  key: string;
  value: string;
};

export type SentryEvent = {
  eventID: string;
  tags: SentryEventTag[];
  dateCreated: string;
  user: null | string;
  message: string;
  title: string;
  id: string;
  platform: string;
  "event.type": string;
  groupID: string;
};

export type SentryIssue = {
  annotations: string[];
  assignedTo: null | string;
  count: string;
  culprit: string;
  firstSeen: string;
  hasSeen: false;
  id: string;
  isBookmarked: false;
  isPublic: false;
  isSubscribed: true;
  lastSeen: string;
  level: string;
  logger: null;
  metadata: { function: string; type: string; value: string; filename: string };
  numComments: number;
  permalink: string;
  project: { platform: string; slug: string; id: string; name: string };
  shareId: null | string;
  shortId: string;
  stats: {
    "24h"?: [number, number][];
    "14d"?: [number, number][];
  };
  status: string;
  statusDetails: {};
  subscriptionDetails: null | string;
  title: string;
  type: string;
  userCount: number;
};

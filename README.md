# gitlab-exporter
GitLab API + Custom Exporter
GitLab API: GitLab's API provides endpoints to get detailed information about projects, commits, merge requests, and more.

* Example API calls:
    * Commits: GET /projects/:id/repository/commits
    * Merge Requests: GET /projects/:id/merge_requests

Custom Exporter:

custom Python script will periodically fetch metrics from the GitLab API and expose them in a format that Prometheus can scrape.

Key Points:

    * Session-Level Headers: By using session.headers.update({'PRIVATE-TOKEN': GITLAB_TOKEN}), the authentication token is set for all requests made through the session. This ensures that each request is properly authenticated.
    * Session Persistence: The session object keeps connections open, reducing the overhead of establishing a new connection for each request, but you must ensure the headers (like the authentication token) are consistently applied.
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

```
# HELP gitlab_commits_total Total number of commits
# TYPE gitlab_commits_total gauge
gitlab_commits_total{project_id="2540"} 11.0
gitlab_commits_total{project_id="2539"} 1.0
gitlab_commits_total{project_id="2538"} 20.0
gitlab_commits_total{project_id="2537"} 20.0
gitlab_commits_total{project_id="2536"} 2.0
gitlab_commits_total{project_id="2535"} 9.0
gitlab_commits_total{project_id="2533"} 2.0
gitlab_commits_total{project_id="2532"} 7.0
gitlab_commits_total{project_id="2531"} 5.0
gitlab_commits_total{project_id="2530"} 4.0
gitlab_commits_total{project_id="2529"} 20.0
gitlab_commits_total{project_id="2528"} 8.0
gitlab_commits_total{project_id="2527"} 20.0
gitlab_commits_total{project_id="2526"} 1.0
gitlab_commits_total{project_id="2525"} 20.0
gitlab_commits_total{project_id="2523"} 20.0
gitlab_commits_total{project_id="2522"} 20.0
gitlab_commits_total{project_id="2520"} 20.0
gitlab_commits_total{project_id="2519"} 0.0
gitlab_commits_total{project_id="2518"} 1.0
# HELP gitlab_merge_requests_total Total number of merge requests
# TYPE gitlab_merge_requests_total gauge
gitlab_merge_requests_total 0.0
# HELP gitlab_project_count Total number of projects
# TYPE gitlab_project_count gauge
gitlab_project_count 0.0
```
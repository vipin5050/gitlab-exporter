import requests
from prometheus_client import start_http_server, Gauge

GITLAB_API_URL = "https://gitlab.wikimedia.org/api/v4"
GITLAB_TOKEN = "your_private_token"
PROJECT_ID = "2244"

commit_gauge = Gauge('gitlab_commits_total', 'Total number of commits', ['project_id'])
merge_request_gauge = Gauge('gitlab_merge_requests_total', 'Total number of merge requests')
project_counts = Gauge('gitlab_project_count', 'Total number of projects')

# Create a session object
session = requests.Session()

def get_projects():
    try:
        response = session.get(f"{GITLAB_API_URL}/projects")
        response.raise_for_status()
        projects = response.json()
        project_ids = [project['id'] for project in projects]
        #print(project_id)
        #return len(response.json())
        return project_ids
        
    except Exception as e:
        print(f"Error fetching commits: {e}")
        return 0

def get_commits(project_id):
    try:
        response = session.get(f"{GITLAB_API_URL}/projects/{project_id}/repository/commits")
        response.raise_for_status()
        return len(response.json())
    except Exception as e:
        print(f"Error fetching commits: {e}")
        return 0

def get_merge_requests(project_id):
    try:
        response = session.get(f"{GITLAB_API_URL}/projects/{project_id}/merge_requests")
        response.raise_for_status()
        return len(response.json())
    except Exception as e:
        print(f"Error fetching merge requests: {e}")
        return 0

def collect_metrics():
    #project_counts.set(get_projects())
    project_ids = get_projects()
    for project_id in project_ids:
        num_commits = get_commits(project_id)
        commit_gauge.labels(project_id=project_id).set(num_commits)
    

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        collect_metrics()

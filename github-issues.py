import json
import requests

with open("vulnerabilities.json", 'r') as file:
    data = json.load(file)

GITHUB_REPO = ""
GITHUB_TOKEN = ""
GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_REPO}/issues"

def create_github_issue(title, body):
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    issue_data = {
        "title": title,
        "body": body,
        "labels": ["vulnerability"]
    }
    
    response = requests.post(GITHUB_API_URL, json=issue_data, headers=headers)
    
    if response.status_code == 201:
        print(f"Issue created: {title}")
    else:
        print(f"Failed to create issue: {response.content}")


max_issues = 10
issue_count = 0

for result in data['Results']:
    for vulnerability in result.get('Vulnerabilities', []):
        if issue_count >= max_issues:
            break  
        title = f"Vulnerability: {vulnerability.get('VulnerabilityID', 'No ID')} in {vulnerability.get('PkgName', 'Unknown Package')}"
        description = vulnerability.get('Description', 'No description available.')
        body = f"""
        **Package:** {vulnerability.get('PkgName', 'Unknown Package')}
        **Vulnerability ID:** {vulnerability.get('VulnerabilityID', 'No ID')}
        **Description:** {description}
        **Severity:** {vulnerability.get('Severity', 'Unknown')}
        **Link:** {vulnerability.get('PrimaryURL', 'No link available')}
        """
        create_github_issue(title, body)
        issue_count += 1 
        
    if issue_count >= max_issues:
        break  



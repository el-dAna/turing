import requests

# Replace these variables with your own values
repo = "username/repo"
token = "your_personal_access_token"
workflow_id = "your_workflow_file.yml"

url = f"https://api.github.com/repos/{repo}/actions/workflows/{workflow_id}/dispatches"
headers = {"Authorization": f"token {token}"}
data = {"ref": "main"}  # Specify the branch to run the workflow on

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print("Workflow triggered successfully!")
else:
    print(f"Failed to trigger workflow: {response.content}")
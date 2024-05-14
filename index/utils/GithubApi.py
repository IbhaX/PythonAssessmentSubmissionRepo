import os
import requests
from dotenv import load_dotenv

from index.schemas.RepoSchema import RepoSchema

load_dotenv()

class GitHubAPI:
    def __init__(self, token=None):
        self.base_url = "https://api.github.com"
        self.token = token or os.getenv("GITHUB_API_TOKEN")
        self.headers = {"Authorization": f"token {token}"} if token else {}

    def search_repo_by_name(self, repo_name):
        url = f"{self.base_url}/search/repositories?q={repo_name}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            results = response.json()['items']
            return [RepoSchema(**i).model_dump() for i in results]
        else:
            print(f"Error: {response.status_code}")

    def get_repo_details(self, username, repo_name):
        url = f"{self.base_url}/repos/{username}/{repo_name}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            from icecream import ic
            ic(response.json())
            return RepoSchema(**response.json()).model_dump()
        else:
            print(f"Error: {response.status_code}")

    def get_user_details(self, username):
        url = f"{self.base_url}/users/{username}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")

def main():
    github = GitHubAPI() 
    repo_details = github.search_repo_by_name("Hello-World")   
    return repo_details


if __name__ == "__main__":
    main()
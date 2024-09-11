import logging

import requests

import cache
import config


def fetch_gitea_repos():
    repos = []
    page = 1
    per_page = 50
    headers = {'Authorization': f'token {config.GITEA_PAT}'}

    logging.info("\nFetching Gitea repositories...")
    while True:
        url = f"{config.GITEA_HOST}/api/v1/user/repos?page={page}&limit={per_page}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            logging.warning(f"Failed to fetch Gitea repositories: {response.status_code} {response.content}")
            break
        page_repos = response.json()
        if not page_repos:
            break
        repos.extend(page_repos)
        page += 1

    logging.info(f"Total Gitea repositories fetched: {len(repos)}")
    return repos


def remove_inexist_repo(github_repos, gitea_repos):
    github_repo_names = {repo["name"] for repo in github_repos}
    for repo in gitea_repos:
        if repo["name"] not in github_repo_names:
            url = f"{config.GITEA_HOST}/api/v1/repos/{repo['owner']['username']}/{repo['name']}"
            headers = {"Authorization": f"token {config.GITEA_PAT}"}
            response = requests.delete(url, headers=headers)
            if response.status_code == 204:
                logging.info(f"Removed removed: {repo['full_name']}")
            else:
                logging.warning(f"Repository removal failed: {repo['full_name']}: {response.status_code} {response.content}")


def check_gitea_repo_exists(repo_name):
    url = f"{config.GITEA_HOST}/api/v1/repos/{repo_name}"
    response = requests.get(url, headers=cache.headers())
    return response.status_code == 200


def remove_gitea_repo(repo_name):
    url = f"{config.GITEA_HOST}/api/v1/repos/{repo_name}"
    response = requests.delete(url, headers=cache.headers())
    if response.status_code == 204:
        logging.info(f"Repository removed: {repo_name}")
    else:
        logging.warning(f"Repository removal failed: {repo_name}: {response.status_code} {response.content}")

import logging

import requests

import cache
import config


def check_gitea_repo_exists(repo_name):
    url = f'{config.GITEA_HOST}/api/v1/repos/{repo_name}'
    response = requests.get(url, headers=cache.headers())
    return response.status_code == 200


def remove_gitea_repo(repo_name):
    url = f'{config.GITEA_HOST}/api/v1/repos/{repo_name}'
    response = requests.delete(url, headers=cache.headers())
    if response.status_code == 204:
        logging.info(f'Repository removed: {repo_name}')
    else:
        logging.warning(f'Repository removal failed: {repo_name}: {response.content}')
